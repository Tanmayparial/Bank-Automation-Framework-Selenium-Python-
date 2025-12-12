import logging
import os

def get_logger(name=__name__):
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    logfile = os.path.join(log_dir, "automation.log")
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        fh = logging.FileHandler(logfile)
        fmt = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    return logger
