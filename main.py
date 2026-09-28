import time

from config import (
    POWERBI_PAGE_DURATION,
    ERROR_RETRY_DELAY,
    MAX_CONSECUTIVE_ERRORS,
)
from logger import setup_logger
from powerpoint import PowerPointController
from powerbi import PowerBIController
from schedule import (
    is_operating_hours,
    wait_until_operating_hours,
)


logger = setup_logger()

def check_environment(
    powerpoint: PowerPointController,
    powerbi: PowerBIController,
) -> None:
    """
    Verifica se os componentes necessários para a automação
    continuam disponíveis.
    """

    if not powerpoint.is_available():
        raise RuntimeError(
            "PowerPoint não está disponível ou "
            "o modo apresentação foi encerrado."
        )

    if not powerbi.browser.is_available():
        raise RuntimeError(
            "Microsoft Edge não está disponível."
        )

def run_cycle(
    powerpoint: PowerPointController,
    powerbi: PowerBIController,
) -> None:
    """
    Executa um ciclo completo da apresentação.
    """

    logger.info("Iniciando ciclo.")

    check_environment(
        powerpoint,
        powerbi
    )

    # PowerPoint
    logger.info("Exibindo apresentação do PowerPoint.")
    powerpoint.show_all_slides()

    # Power BI
    logger.info("Abrindo Power BI.")
    powerbi.open()

    if powerbi.needs_refresh():
        logger.info("Power BI precisa ser atualizado.")
        powerbi.refresh()

    logger.info("Entrando em tela cheia no Power BI.")
    powerbi.enter_fullscreen()

    logger.info("Exibindo dashboard: Prioridades.")
    powerbi.show_prioridades()
    time.sleep(POWERBI_PAGE_DURATION)

    logger.info("Exibindo dashboard: A vencer em 3 dias.")
    powerbi.show_a_vencer_3_dias()
    time.sleep(POWERBI_PAGE_DURATION)

    logger.info("Saindo da tela cheia do Power BI.")
    powerbi.exit_fullscreen()

    # Prepara o PowerPoint para o próximo ciclo.
    powerpoint.first_slide()

    logger.info("Voltando ao PowerPoint.")
    powerpoint.focus()

    logger.info("Ciclo concluído com sucesso.")


def recover(
    powerpoint: PowerPointController,
    powerbi: PowerBIController,
) -> None:
    """
    Tenta retornar a aplicação a um estado conhecido
    após alguma falha.
    """

    logger.warning("Tentando recuperar estado da apresentação.")

    # Primeiro tentamos sair de qualquer tela cheia/menu
    # que possa ter ficado aberto no Power BI.
    try:
        powerbi.exit_fullscreen()
    except Exception:
        logger.warning(
            "Não foi possível sair do modo tela cheia do Power BI."
        )

    # Depois tentamos retornar ao PowerPoint.
    try:
        powerpoint.first_slide()
        powerpoint.focus()

        logger.info(
            "Recuperação concluída: PowerPoint no primeiro slide."
        )

    except Exception:
        logger.exception(
            "Não foi possível recuperar o PowerPoint."
        )


def main() -> None:
    logger.info("Aplicação iniciada.")

    if not wait_until_operating_hours():
        logger.info(
            "Aplicação encerrada fora do horário de funcionamento."
        )
        return

    powerpoint = PowerPointController()
    powerbi = PowerBIController()

    consecutive_errors = 0

    logger.info("Automação da TV iniciada.")

    while is_operating_hours():
        try:
            run_cycle(
                powerpoint,
                powerbi,
            )

            # Se o ciclo terminou corretamente,
            # zeramos o contador de falhas.
            consecutive_errors = 0

        except KeyboardInterrupt:
            logger.info(
                "Automação interrompida manualmente."
            )
            break

        except Exception:
            consecutive_errors += 1

            logger.exception(
                "Erro durante o ciclo. "
                f"Falhas consecutivas: "
                f"{consecutive_errors}/"
                f"{MAX_CONSECUTIVE_ERRORS}"
            )

            recover(
                powerpoint,
                powerbi,
            )

            if consecutive_errors >= MAX_CONSECUTIVE_ERRORS:
                logger.critical(
                    "Número máximo de falhas consecutivas "
                    "atingido. Encerrando aplicação."
                )
                break

            logger.info(
                f"Nova tentativa em "
                f"{ERROR_RETRY_DELAY} segundos."
            )

            time.sleep(ERROR_RETRY_DELAY)

    logger.info("Automação encerrada.")


if __name__ == "__main__":
    main()