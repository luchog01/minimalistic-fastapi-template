import logging
import sys
from datetime import datetime

from api.core.config import settings


class SimpleFormatter(logging.Formatter):
    """Simple formatter with colored output for console."""

    COLORS = {
        "DEBUG": "\033[36m",  # Cyan
        "INFO": "\033[32m",  # Green
        "WARNING": "\033[33m",  # Yellow
        "ERROR": "\033[31m",  # Red
        "RESET": "\033[0m",  # Reset
    }

    def format(self, record: logging.LogRecord) -> str:
        color = self.COLORS.get(record.levelname, "")
        reset = self.COLORS["RESET"]

        # Format: [time] [level] [module:line] message
        return (
            f"{color}[{datetime.now().strftime('%H:%M:%S')}] "
            f"[{record.levelname}] [{record.name}:{record.lineno}] "
            f"{record.getMessage()}{reset}"
        )


def setup_logging() -> None:
    """Set up logging configuration."""
    # Create and configure console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(SimpleFormatter())

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)
    root_logger.addHandler(console_handler)

    # Configure uvicorn loggers
    for logger_name in ("uvicorn", "uvicorn.access", "uvicorn.error"):
        logger = logging.getLogger(logger_name)
        logger.handlers = [console_handler]


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance."""
    return logging.getLogger(name)
