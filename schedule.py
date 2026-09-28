import time
from datetime import datetime

from config import (
    START_TIME,
    END_TIME,
    OPERATING_WEEKDAYS,
    TEST_MODE,
)


def is_operating_hours() -> bool:
    """
    Retorna True quando a automação pode executar ciclos.

    Em TEST_MODE, ignora horário e dia da semana.
    """
    if TEST_MODE:
        return True

    now = datetime.now()

    return (
        now.weekday() in OPERATING_WEEKDAYS
        and START_TIME <= now.time() < END_TIME
    )


def wait_until_operating_hours() -> None:
    """
    Mantém a aplicação aguardando até chegar
    ao próximo período de funcionamento.
    """
    while not is_operating_hours():
        now = datetime.now()

        print(
            f"Fora do horário de funcionamento "
            f"({now:%d/%m/%Y %H:%M}). Aguardando..."
        )

        time.sleep(60)