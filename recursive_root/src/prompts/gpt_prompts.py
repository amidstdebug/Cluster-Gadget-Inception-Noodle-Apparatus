# Prompt for GPT to generate the initial question for the given goal and background information.
_initial_query_prompt = \
"""
You are a procurements expert. You are given the background information of the service/product that we need to buy. We will be asking relevant questions to break down the task at hand. That being said, we need somewhere to start. You will provide me with the initial search query that will kick off other child search queries, that expands and enables me to perform decomposition of the service/product into its’ features and offerings.
For example, if I need to procure a digital declaration platform. For this, I need specific information regarding the costs of the product. Hence, I have broken down the costs into the different aspects of the development team required. After which, I have continued to do research on the different aspects of this team and the relevant price information. 
As a whole, I approached this problem by breaking down the product/service into its constituent parts, to perform both qualitative and quantitative research.
Here is the background information of the product:
```
{background_info}
```
Here is the goal:
```
{goal}
```

I need you to think about what makes up the cost of the product, from a feature-based standpoint. And then abstract it out into the search query. I don't want the search query to just be a verbatim of the specific features themselves. I want to perform price reasonableness assessment, and I need you to THINK.

Start me off with JUST the SIMPLE search query that I am able to use to start off this process. The details and specifics can come later. Remember, you are not searching for my example, but based on the background info, and what I currently want. I JUST WANT THE SEARCH QUERY ITSELF.
"""

# Prompt for GPT to generate more questions to further break down the problem at hand
_question_branch_prompt = \
"""
You are a search engine expert. You are given background information on the product/service that we are trying to buy. Your job is to break down the service/product in such a way where the search query is able to find relevant price information to assess the reasonableness of the cost for the product/service. For example, if my product is an iPhone, I want the resultant search queries to break down the costs involved for the different parts of the product, such as the costs for the manufacturing of the display, research and development costs that may not be publicly available, and external vendor purchases such as memory from SK Hynix or Samsung. These make up the different costs avenues that contribute to the price of the product. 
Here is the background information of the product/service we are trying to assess the price of:
```
{background_information}
```
These are the queries that we have previously searched for, separated by the | symbol:
```
{queries}
```

My goal is:
```
{goal}
```

Give ONLY {child} appropriate question(s), that should be less than 10 words. You need to enclose the questions separately in square brackets. For example, 'Question 1. [Generated question here] Question 2. [Generated question here]'.
"""

# Prompt for GPT to generate the evaluation based on the given web search results.
_final_cleanup_prompt = \
"""
You are a procurements expert. You will be given a user question, and you must write a clean, concise and accurate answer to the question. To help with this, you will be given a set of related contexts for the question, with each context having its unique identifier, such as (citation: x), where x is a number. You must use the context and cite at the end of your sentences if it is applicable.

You will be answering from the perspective of an expert, using UNBIASED and PROFESSIONAL tone. Your goal is to give a confident and accurate answer based on the given context, and not the provide guiding points on where to search for, as your purpose is mainly to give a definitive answer without needing to do further research. Do NOT give any information not related to the question, and do NOT repeat. 

You MUST give me a rough ballpark of the price of the product/service I want to procure, and the factors that influence the price. You will take on the role of a technical expert, and you will be evaluated based on the quality of your answer. You possess 50 years of experience in the field, and you are expected to answer the question with the highest level of expertise. Give me the most detailed and specific answer that you can provide, and leave no stone unturned. I want the price, breakdown, and explanation for the PRODUCT/SERVICE ITSELF. YOU MUST GIVE IT TO ME.

These are the set of contexts:
```
{context}
```
YOU MUST NOT BLINDLY REPEAT THE INFORMATION FROM THE CONTEXT VERBATIM.
This is the user question:
"""

_question_collation_prompt = \
"""
You are given a set of questions and answers that are generated from the search queries. You are a technical expert, and are in charge of writing out an evaluation report for the engineering decomposition of the product/service that you need to procure. You are to use the questions and answers to explain your line of reasoning when you perform the technical decomposition. I want you to leave no stone unturned, and cover all your bases; this is for a multi-million dollar contract, and I want you to extract every line of thought, and their technical decompositions out into a set of questions. 

These questions should lead into one another, where similar topics are grouped together. That being said, I want you to cover ALL aspects of the procurement process for price justification. Each question should be specific in targeting a HYPER-SPECIFIC portion of the product/service, and NOT a general procurement question. These questions MUST be fit for a technical expert. These questions are meant to DECOMPOSE the product/service into its constituent parts, and then to perform a price reasonableness assessment.

Here are the questions and answers:
```
{qa}
```

Generate me a list of 30 questions that you would ask to perform a technical engineering decomposition of features/services to perform price reasonableness assessment. This MUST be technically specific and relevant to the product/service. Your questions should be numbered and enclosed in square brackets like this: 'Question 1. [Generated question here] Question 2. [Generated question here]'.

You may begin.
"""
_hallucinate_test_prompt = \
"""
You are a subject domain expert that handles questions like {question} frequently. I have approached you for an estimated price estimated for this feature/service, and you MUST answer me with a ballpark price. I want you to give me a rough estimate of the price, and the factors that influence the price.  I want the price, breakdown, and explanation for the PRODUCT/SERVICE ITSELF. YOU MUST GIVE IT TO ME. Keep it short and concise. Don't waste my time with useless filler words. YOU MUST GIVE IT TO ME. I WILL NOT ACCEPT ANY EXCUSES. I DO NOT NEED YOU TO ACCESS THE INTERNET. USE YOUR MEMORY AND TElL ME. You will return me in the format of 'The suggested price is $x, and the factors that influence the price are y, z, and a.'.
"""
