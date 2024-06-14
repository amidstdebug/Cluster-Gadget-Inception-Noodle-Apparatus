import os
from dotenv import load_dotenv

load_dotenv()

DEPLOYMENT = os.getenv("DEPLOYMENT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_VERSION = os.getenv("AZURE_OPENAI_VERSION")
EMBEDDING_OPENAI_KEY = os.getenv("EMBEDDING_OPENAI_KEY")
BING_API_KEY = os.getenv("BING_API_KEY")
