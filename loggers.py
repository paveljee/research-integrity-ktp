import logging

def get_logger(name=__name__, log_file=None, level=logging.INFO):
    if not log_file:
        log_file = f"logs/{name}.log"
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:  # prevent duplicate handlers
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter("[%(levelname)s] %(message)s")
        console_handler.setFormatter(console_formatter)

        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
