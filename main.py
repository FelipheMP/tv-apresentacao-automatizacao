import time

from powerpoint import PowerPointController
from powerbi import PowerBIController


def main() -> None:
    powerpoint = PowerPointController()
    powerbi = PowerBIController()

    print("PowerPoint...")
    powerpoint.focus()

    time.sleep(3)

    print("Abrindo Power BI...")
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

    print("Teste concluído.")


if __name__ == "__main__":
    main()