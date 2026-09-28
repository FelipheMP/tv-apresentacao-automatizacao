import time
from datetime import datetime

from config import (
    START_TIME,
    END_TIME,
    OPERATING_WEEKDAYS,
    TEST_MODE
)


def is_weekday() -> bool:
    """Retorna True se hoje for um dia útil configurado."""
    return datetime.now().weekday() in OPERATING_WEEKDAYS

def is_operating_hours() -> bool:
    """
    Retorna True quando estamos em um dia útil
    e dentro do horário de funcionamento.

    Em TEST_MODE, ignora essas restrições.
    """
    if TEST_MODE:
        return True

    now = datetime.now()

    return (
        now.weekday() in OPERATING_WEEKDAYS
        and START_TIME <= now.time() < END_TIME
    )

def wait_until_operating_hours() -> bool:
    """
    Aguarda até o início do horário operacional.

    Em TEST_MODE, libera imediatamente.
    """
    if TEST_MODE:
        print("Modo de teste ativo: ignorando horário e dia útil.")
        return True

    while True:
        now = datetime.now()

        if now.weekday() not in OPERATING_WEEKDAYS:
            print("Hoje não é um dia de funcionamento.")
            return False

        if now.time() >= END_TIME:
            print("O horário de funcionamento de hoje já terminou.")
            return False

        if START_TIME <= now.time() < END_TIME:
            return True

        print("Aguardando horário de funcionamento...")
        time.sleep(30)