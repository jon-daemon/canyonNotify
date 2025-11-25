from config import bike_map, log_level
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=log_level
)

logger = logging.getLogger(__name__)

def update():
    """Check all bikes and return True if any changed."""
    changed = False
    for bike in bike_map:
        changed |= bike.update()
    return changed

def status():
    """Return string summary of all bikes."""
    output = ""
    for bike in bike_map:
        output += f"{'YES' if bike.avail else 'NO'} - {bike.name}: {'available' if bike.avail else 'UNavailable'} in size {bike.size}\n"
    return output
