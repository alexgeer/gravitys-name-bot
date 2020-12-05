from config import create_api
from names import getName

from logger import logger

api = create_api()
name = getName()

try:
    # api.update_status(name)
    logger.info(name)
except Exception as e:
    logger.error("Error status update", exc_info=True)