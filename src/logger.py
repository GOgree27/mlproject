import os
import logging

# Ensure the 'log' directory exists
log_dir = "log"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure the logger
log_file = os.path.join(log_dir, "app.log")
logging.basicConfig(
    filename=log_file,  # Log file path
    level=logging.DEBUG,  # Log level
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log format
)

# Create a logger object
logger = logging.getLogger("my_logger")

# Example log messages
logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")
