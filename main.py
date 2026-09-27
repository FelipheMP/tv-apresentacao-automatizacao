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

    time.sleep(5)

    print("Saindo da tela cheia...")
    powerbi.exit_fullscreen()

    time.sleep(2)

    print("Voltando ao PowerPoint...")
    powerpoint.focus()

    print("Teste concluído.")


if __name__ == "__main__":
    main()