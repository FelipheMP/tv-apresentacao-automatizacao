import time

from powerpoint import PowerPointController
from powerbi import PowerBIController
from schedule import (
    is_operating_hours,
    wait_until_operating_hours,
)


def run_cycle(
    powerpoint: PowerPointController,
    powerbi: PowerBIController,
) -> None:
    """
    Executa um ciclo simples da automação.
    """

    print("PowerPoint...")
    powerpoint.focus()

    time.sleep(3)

    print("Power BI...")
    powerbi.open()

    if powerbi.needs_refresh():
        powerbi.refresh()

    print("Entrando em tela cheia...")
    powerbi.enter_fullscreen()

    print("Mostrando Prioridades...")
    powerbi.show_prioridades()
    time.sleep(5)

    print("Mostrando A vencer em 3 dias...")
    powerbi.show_a_vencer_3_dias()
    time.sleep(5)

    print("Saindo da tela cheia...")
    powerbi.exit_fullscreen()

    print("Voltando ao PowerPoint...")
    powerpoint.focus()


def main() -> None:
    if not wait_until_operating_hours():
        return

    powerpoint = PowerPointController()
    powerbi = PowerBIController()

    print("Automação iniciada.")

    while is_operating_hours():
        run_cycle(powerpoint, powerbi)

    print("Horário de funcionamento encerrado.")


if __name__ == "__main__":
    main()