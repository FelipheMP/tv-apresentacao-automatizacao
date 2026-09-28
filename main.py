import time

from powerpoint import PowerPointController
from powerbi import PowerBIController


def main() -> None:
    powerpoint = PowerPointController()
    powerbi = PowerBIController()

    print("PowerPoint...")
    powerpoint.focus()

    time.sleep(3)

    print("Power BI...")
    powerbi.open()

    time.sleep(2)

    print("Entrando em tela cheia...")
    powerbi.enter_fullscreen()

    time.sleep(3)

    print("Mostrando Prioridades...")
    powerbi.show_prioridades()
    time.sleep(5)

    print("Mostrando A vencer em 3 dias...")
    powerbi.show_a_vencer_3_dias()

    time.sleep(5)

    print("Saindo da tela cheia...")
    powerbi.exit_fullscreen()

    time.sleep(2)

    print("Voltando ao PowerPoint...")
    powerpoint.focus()

    print("Teste concluído.")


if __name__ == "__main__":
    main()