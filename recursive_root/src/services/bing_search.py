import time
import logging

from requests import RequestException

from recursive_root.src.utils.requests import make_request
from recursive_root.src.config import BING_API_KEY

def search_with_bing(query, subscription_key=BING_API_KEY):
    BING_SEARCH_V7_ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"
    BING_MKT = "en-US"
    DEFAULT_SEARCH_ENGINE_TIMEOUT = 20
    REFERENCE_COUNT = 10
    MAX_RETRIES = 5
    RETRY_DELAY = 2

    params = {
        "q": query,
        "mkt": BING_MKT,
        "responseFilter": "Webpages",
        "count": 3
    }

    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
    }

    for attempt in range(MAX_RETRIES):
        try:
            if params['q'].startswith('"'):
                params['q'] = params['q'][1:]
            if params['q'].endswith('"'):
                params['q'] = params['q'][:-1]

            response = make_request(BING_SEARCH_V7_ENDPOINT, params=params, headers=headers)
            contexts = response.get("webPages", {}).get("value", [])[:REFERENCE_COUNT]

            if not contexts:
                # Handle no contexts found
                logging.error(f"No contexts found in response for query: '{params['q']}'")
                time.sleep(RETRY_DELAY)
                continue

            return contexts

        except RequestException as e:
            logging.error(f"Request failed: {e}")
            if attempt < MAX_RETRIES - 1:
                time.sleep(RETRY_DELAY)
                continue
            else:
                return []

    logging.error("All retries failed.")
    return []
