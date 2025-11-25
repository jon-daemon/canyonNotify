import time
import parser
import notify
import config
import logging

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting bike checker with Pushover notifications")

    while True:
        if parser.update():
            message = parser.status()
            notify.pushover(message)
            logger.info("Change detected, notification sent")
        else:
            logger.info("No changes")

        time.sleep(config.interval)

if __name__ == "__main__":
    main()
