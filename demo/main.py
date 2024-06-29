from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.routes.router import api_router
from src.core.config import (API_PREFIX, APP_NAME, APP_VERSION, API_PORT, API_VERSION, IS_DEBUG)
import uvicorn

def get_app() -> FastAPI:
	fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)

	fast_app.add_middleware(
		CORSMiddleware,
		allow_origins=["*"],
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"]
	)
	fast_app.include_router(router = api_router)

	return fast_app

app = get_app()

# allow_origins=[*] is not recommended for Production purposes.
# It is recommended to have specified list of origins such as mentioned below:
# allow_origins=['client-facing-example-app.com', 'localhost:5000']
if __name__ == '__main__':
	# Listening on all network interfaces: 0.0.0.0
	uvicorn.run("main:app", host="0.0.0.0", port=API_PORT)