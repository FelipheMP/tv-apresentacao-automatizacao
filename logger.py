import logging
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "tv_dashboard.log"


def setup_logger() -> logging.Logger:
    """
    Configura o logger da aplicação.

    Os logs são exibidos no terminal e também salvos em arquivo.
    """
    LOG_DIR.mkdir(exist_ok=True)

    logger = logging.getLogger("tv_dashboard")
    logger.setLevel(logging.INFO)

    # Evita adicionar handlers duplicados caso a função
    # seja chamada mais de uma vez.
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8",
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger