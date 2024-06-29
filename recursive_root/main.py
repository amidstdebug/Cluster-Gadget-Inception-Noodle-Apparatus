import logging

from src.services.bing_search import search_with_bing
from src.utils.logging import setup_logging
from src.config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_VERSION, EMBEDDING_OPENAI_KEY,BING_API_KEY, DEPLOYMENT
from src.services.openai_service import OpenAIService
from src.models.researcher import OptimisedResearcher
from src.analysis.data_cleaning import clean_final_information, create_qa_context
from src.analysis.embeddings import EmbeddingAnalysis
from src.analysis.qdrant_management import QdrantManager
from src.analysis.final_cleanup import final_cleanup
from src.prompts.gpt_prompts import _final_cleanup_prompt


def main():
	setup_logging()  # Initialize logging configuration
	logging.info("Starting application")

	goal = "procure a sim racing system"
	max_depth = 2
	max_child = 2
	bg_info = "I know about fanatec and thrustmaster"
	openai_service = OpenAIService(AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY,AZURE_OPENAI_VERSION,DEPLOYMENT)
	researcher = OptimisedResearcher(goal, max_depth,max_child, bg_info, openai_service=openai_service)
	initial_query = True
	results = researcher.explore(query_generator=initial_query)

	result_hold = final_cleanup(results, bg_info,goal, _final_cleanup_prompt,openai_service)

	# final_information_cleaned = clean_final_information(results)
	# qa_context = create_qa_context(final_information_cleaned)
	#
	# embedding_analysis = EmbeddingAnalysis()
	# query_embeddings = embedding_analysis.get_embeddings(qa_context['Query'].tolist())
	# snippet_embeddings = embedding_analysis.get_embeddings(qa_context['Context'].tolist())
	#
	# qdrant_manager = QdrantManager()
	# qdrant_manager.upsert_embeddings(snippet_embeddings, qa_context['Context'].tolist())
	#
	# for query_embedding in query_embeddings[:5]:
	# 	similar_results = qdrant_manager.search_similar(query_embedding)
	# 	for result in similar_results:
	# 		logging.info(f"Score: {result.score}, Snippet: {result.payload['snippet']}")


if __name__ == "__main__":
	main()
