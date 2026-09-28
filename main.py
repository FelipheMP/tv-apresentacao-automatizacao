import time

from config import POWERBI_PAGE_DURATION
from powerpoint import PowerPointController
from powerbi import PowerBIController
from schedule import (
    is_operating_hours,
    wait_until_operating_hours
)


def run_cycle(
    powerpoint: PowerPointController,
    powerbi: PowerBIController,
) -> None:
    """
    Executa um ciclo completo da exibição da TV.

    1. Exibe todos os slides do PowerPoint.
    2. Abre o Power BI.
    3. Atualiza o relatório quando necessário.
    4. Exibe Prioridades.
    5. Exibe A vencer em 3 dias.
    6. Retorna ao primeiro slide do PowerPoint.
    """

    print("\n--- Iniciando ciclo ---")

    # PowerPoint
    powerpoint.show_all_slides()

    # Power BI
    print("Abrindo Power BI...")
    powerbi.open()

    if powerbi.needs_refresh():
        powerbi.refresh()

    print("Entrando em tela cheia...")
    powerbi.enter_fullscreen()

    print("Exibindo Prioridades...")
    powerbi.show_prioridades()
    time.sleep(POWERBI_PAGE_DURATION)

    print("Exibindo A vencer em 3 dias...")
    powerbi.show_a_vencer_3_dias()
    time.sleep(POWERBI_PAGE_DURATION)

    print("Saindo da tela cheia...")
    powerbi.exit_fullscreen()

    # Prepara o PowerPoint para o próximo ciclo antes
    # de colocá-lo novamente na frente.
    powerpoint.first_slide()

    print("Voltando ao PowerPoint...")
    powerpoint.focus()

    print("--- Ciclo concluído ---")

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