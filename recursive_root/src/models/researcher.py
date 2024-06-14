import re
import time

from anytree import Node
from src.services.bing_search import search_with_bing
from src.prompts.gpt_prompts import _question_branch_prompt, _initial_query_prompt

class OptimisedResearcher:
    def __init__(self, goal, max_depth, max_child, bg_info, openai_service, query=None, previous_node=None, depth=0, label=''):
        self.goal = goal
        self.max_depth = max_depth
        self.query = None if previous_node is None else Node(query, parent=previous_node)
        self.depth = depth
        self.bg_info = bg_info
        self.max_child = max_child
        self.label = label
        self.openai_service = openai_service

    def perform_search(self, query):
        results = search_with_bing(query)
        return [{**i, "query": query} for i in results]

    def post_process(self, content):
        pattern = r"\[(.*?)\]"
        matches = re.findall(pattern, content)
        return matches

    def process_results(self):
        user_prompt = _question_branch_prompt.format(
            background_information=self.bg_info,
            queries="|".join(self.get_parent_history(self.query)),
            child=f"{self.max_child}",
            goal=self.goal,
        )

        llm_response = self.openai_service.generate_response(max_tokens=1024, system_prompt=None, user_prompt=user_prompt)
        time.sleep(3)
        return self.post_process(llm_response)

    def get_parent_history(self, node):
        values = []
        while node is not None:
            values.append(node.name)
            node = node.parent
        return values[::-1]

    def explore(self, query_generator):
        aggregated_information = []

        if self.depth < self.max_depth:
            if query_generator:
                query_response = self.openai_service.generate_response(
                    max_tokens=1024,
                    system_prompt=None,
                    user_prompt=_initial_query_prompt.format(
                        background_info=f"{self.bg_info}",
                        goal=self.goal
                    )
                )
                # prevent rate limit
                time.sleep(5)

                self.query = Node(query_response)
                print("\n", "(Generated Query) Searched for:", query_response)

                results = self.perform_search(query_response)
            else:
                results = self.perform_search(self.query.name)
                print("\n", self.label, "Searched for:", self.query.name)

            if results:
                new_queries = self.process_results()
                aggregated_information.extend(results)
                future_tasks = []
                for i, query in enumerate(new_queries[:self.max_child]):
                    if self.depth + 1 < self.max_depth:
                        label = self.label + chr(65 + i)
                        future_tasks.append(self.create_child_and_explore(query, label))

                for future in future_tasks:
                    aggregated_information.extend(future)
        return aggregated_information

    def create_child_and_explore(self, query, label):
        child = OptimisedResearcher(self.goal, self.max_depth,
                                    self.max_child, self.bg_info,
                                    self.openai_service, query=query,
                                    previous_node=self.query,
                                    depth=self.depth + 1, label=label)
        return child.explore(query_generator=False)
