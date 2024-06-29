from starlette.config import Config
from starlette.datastructures import Secret

APP_VERSION = "1.0"
APP_NAME = "Procurement Service"

config = Config(".env")

IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)
API_VERSION: str = config("API_VERSION", cast=str, default="v1")
API_PORT: int = config("API_PORT", cast=int, default=10000)
API_THREADS: int = config("API_THREADS", cast=int, default = 3) # Note that each API thread will NOT lead to hotload VRAM usage, but will lead to additional inference VRAM usage.

# Using config instead
DEPLOYMENT = config("DEPLOYMENT", default="local")
AZURE_OPENAI_KEY = config("AZURE_OPENAI_KEY", default=None)
AZURE_OPENAI_ENDPOINT = config("AZURE_OPENAI_ENDPOINT", default=None)
AZURE_OPENAI_VERSION = config("AZURE_OPENAI_VERSION", default=None)
EMBEDDING_OPENAI_KEY = config("EMBEDDING_OPENAI_KEY", default = None)
BING_API_KEY = config("BING_API_KEY", default=None)

API_PREFIX = "/{}/bccaas".format(API_VERSION)  #"/api"