import random
import tiktoken
from openai import AzureOpenAI
from src.config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_VERSION, EMBEDDING_OPENAI_KEY,BING_API_KEY, DEPLOYMENT


def final_cleanup(fi, background_info, goal, final_cleanup_prompt, openai_service):
	encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

	max_tokens = 4000
	instructions = f"Using the information above as context, and given the information provided here: {background_info}, answer the question {goal}. I don't need you to tell me what to do. Be AS SPECIFIC AS POSSIBLE. The product/service pricing decomposition is the MOST IMPORTANT TO ME. Your answer should be final and not require any further actions from me, if not I wouldn't be asking you any of this. Provide the breakdown and cost estimates of the individual components in MARKDOWN TABLE FORMAT. I dont need it to be exact. Even if you don't have all the information, just give an ESTIMATE. I want you to ESTIMATE the costs for the components."

	# Rare occurrence where Bing Search provides even more detailed information.
	# If that is the case, we parse this extra information and add into snippet.
	for i in range(len(fi)):
		if "richFacts" in fi[i]:
			fi[i]["snippet"] = fi[i][
				                   "snippet"] + f"metadata: {','.join([j['label']['text'] + ' : ' + j['items'][0]['text'] for j in fi[i]['richFacts']])}"

	# Randomly sample snippets, until we hit the token limit of the GPT model
	rand_list = list(range(len(fi)))
	random.shuffle(rand_list)
	new_fi = []
	s = len(encoding.encode(instructions)) + len(encoding.encode(final_cleanup_prompt))
	arr = [len(encoding.encode(r['snippet'])) + len(encoding.encode(f"(citation:{i + 1}) ")) for i, r in enumerate(fi)]
	for i in rand_list:
		if s + arr[i] > (8192 - max_tokens):
			break
		s += arr[i]
		new_fi.append(fi[i])

	# Once we have the list of the sampled snippets, which all fit within the context length, we extract the information
	# and form a final response
	system_prompt = final_cleanup_prompt.format(
		context="\n\n".join(
			[f"(citation:{i + 1}) {f['snippet']}" for i, f in enumerate(new_fi)]
		)
	)
	try:
		llm_response = openai_service.generate_response(
			max_tokens,system_prompt, instructions
		)
	except Exception as e:
		return [None,
		        system_prompt + "\n" + f"Using the information above, and given the information provided here: {background_info}, answer the question {goal}. I don't need you to tell me what to do. You are a procurement expert, and all I need is for you to answer the question and LEAVE IT AT THAT."]

	print('\n\x1b[35mFinal response\x1b[0m:')
	return [llm_response, system_prompt]
