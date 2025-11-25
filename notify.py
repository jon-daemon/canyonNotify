import requests
import config
import logging

logger = logging.getLogger(__name__)

def pushover(message: str):
    """Send notification to Pushover."""
    data = {
        "token": config.pushover_api_token,
        "user": config.pushover_user_key,
        "message": message
    }

    try:
        response = requests.post("https://api.pushover.net/1/messages.json", data=data)
        response.raise_for_status()
        logger.info("Pushover notification sent")
    except Exception as e:
        logger.error(f"Failed to send Pushover notification: {e}")
