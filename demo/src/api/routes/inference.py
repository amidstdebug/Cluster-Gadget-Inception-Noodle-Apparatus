from fastapi import APIRouter
from fastapi import HTTPException
from starlette.requests import Request
import anyio

#from src.core import security
from src.interface.payload import Payload
from src.interface.response import Results

import sys
sys.path.insert(0, '/backend')
# from src.services.openai_service import OpenAIService
from recursive_root.src.services.openai_service import OpenAIService
from recursive_root.src.models.researcher import OptimisedResearcher
from recursive_root.src.analysis.final_cleanup import final_cleanup
from recursive_root.src.prompts.gpt_prompts import _final_cleanup_prompt

from src.core.config import AZURE_OPENAI_KEY, AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_VERSION, DEPLOYMENT


router = APIRouter()

@router.post("/infer", response_model = Results, name="inference")
async def post_inference(
	request: Request,
) -> Results:

	try:
		req_json = await request.json()
		block_data = Payload(**req_json)
	except Exception as e:
		print("Error:", e)
		raise HTTPException(status_code=422, detail="Unable to process json. Format is incorrect.")

	# goal = "procure a sim racing system"
	# max_depth = 2
	# max_child = 2
	# bg_info = "I know about fanatec and thrustmaster"
	openai_service = OpenAIService(AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY,AZURE_OPENAI_VERSION,DEPLOYMENT)
	researcher = OptimisedResearcher(
		block_data.goal,
		block_data.max_depth,
		block_data.max_nodes,
		block_data.background,
		openai_service=openai_service
	)

	initial_query = True
	results = researcher.explore(query_generator=initial_query)

	result_hold = final_cleanup(results, block_data.background, block_data.goal, _final_cleanup_prompt, openai_service)

	return {'output': result_hold}