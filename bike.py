from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)

class Bike:
    def __init__(self, name, link, size="L"):
        self.name = name
        self.link = link
        self.size = size
        self.avail = False
        logger.info(f'{name} is created')

    def update(self):
        """Check availability and return True if changed."""
        new_avail = self.parse_url()
        changed = (self.avail != new_avail)
        self.avail = new_avail

        logger.info(f'{self.name} status {"changed" if changed else "NOT changed"}')
        return changed

    def parse_url(self):
        req = requests.get(self.link)
        soup = BeautifulSoup(req.text, "html.parser")

        # Every size button has data-product-size="M", "L", "XL", etc.
        size_buttons = soup.select('button[data-product-size]')
        logger.info(f'{self.name} parse found {len(size_buttons)} size buttons')

        for btn in size_buttons:
            size_value = btn.get("data-product-size", "").strip()

            # logger.info(f"Found size button: {size_value}")

            if size_value == self.size:
                # Check availability: purchasable buttons are not labeled with unpurchasable classes
                classes = btn.get("class", [])
                unavailable = any("unpurchasable" in c for c in classes)

                if not unavailable:
                    logger.info(f'{self.name} IS AVAILABLE in size {self.size}')
                    return True
                else:
                    logger.info(f'{self.name} is NOT available in size {self.size}')
                    return False

        logger.info(f'{self.name} size {self.size} not found')
        return False