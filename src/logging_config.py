import logging
import os

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_logger(name: str, log_file: str, level: int = logging.INFO) -> logging.Logger:
    """Настройка логгера для записи в отдельный файл."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    file_handler = logging.FileHandler(os.path.join(LOG_DIR, log_file), mode="w")
    file_handler.setFormatter(logging.Formatter(LOG_FORMAT))

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)

    return logger


masks_logger = setup_logger("masks", "masks.log", logging.DEBUG)
utils_logger = setup_logger("utils", "utils.log", logging.DEBUG)
