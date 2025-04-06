"""Logger configuration"""

import logging

FORMAT = "[%(asctime)s] | %(levelname)s | [%(filename)s:%(lineno)d] | MESSAGE: %(message)s"


logging.basicConfig(
    level="INFO",
    format=FORMAT,
    datefmt="%m/%d/%Y %I:%M:%S %p",
)

# Suppress logs from httpx and other libraries
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)
