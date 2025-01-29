from rich.console import Console
from rich.logging import RichHandler
import logging

# Initialize Rich console
console = Console()

# Configure logging with Rich
logging.basicConfig(
    level=logging.DEBUG,  # Set log level
    format="%(message)s",  # Simple message format
    handlers=[RichHandler()],  # Use Rich's logging handler
)

# Create logger
logger = logging.getLogger("rich")

# Function to log messages


def log_info(message: str) -> None:
    logger.info(message)


def log_warning(message: str) -> None:
    logger.warning(message)


def log_error(message: str) -> None:
    logger.error(message)


def log_critical(message: str) -> None:
    logger.critical(message)
