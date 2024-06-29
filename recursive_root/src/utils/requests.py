import requests
from requests.exceptions import RequestException
import logging
from recursive_root.src.utils.logging import setup_logging

# Call the setup_logging function to configure logging
setup_logging()

def make_request(url, params=None, headers=None, timeout=20):
    try:
        response = requests.get(url, params=params, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        logging.error(f"Request failed: {e}")
        return None
