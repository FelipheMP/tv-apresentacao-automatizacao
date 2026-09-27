import time

import pyautogui

from browser import BrowserController
from config import (
    POWERBI_VIEW_MENU,
    POWERBI_FULLSCREEN_OPTION,
    POWERBI_PAGE_MENU,
    POWERBI_PAGE_PRIORIDADES,
    POWERBI_PAGE_A_VENCER,
    POWERBI_UI_DELAY,
)


class PowerBIController:
    """
    Responsável por controlar o Power BI aberto no Microsoft Edge.
    """

    def __init__(self):
        self.browser = BrowserController()

    def open(self) -> None:
        """Traz o Edge com o Power BI para frente."""
        self.browser.focus()

    def _click(self, position: tuple[int, int]) -> None:
        """
        Move o cursor até uma coordenada e realiza um clique.
        """
        x, y = position

        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()

        time.sleep(POWERBI_UI_DELAY)

    def enter_fullscreen(self) -> None:
        """
        Entra no modo tela cheia do Power BI.

        Fluxo:
        1. Abre o menu de exibição.
        2. Clica na opção de tela cheia.
        """
        self._click(POWERBI_VIEW_MENU)
        self._click(POWERBI_FULLSCREEN_OPTION)

    def exit_fullscreen(self) -> None:
        """Sai do modo tela cheia."""
        pyautogui.press("esc")
        time.sleep(POWERBI_UI_DELAY)

    def show_prioridades(self) -> None:
        """
        Abre a página 'Prioridades' pelo menu inferior.
        """
        self._click(POWERBI_PAGE_MENU)
        self._click(POWERBI_PAGE_PRIORIDADES)

    def show_a_vencer_3_dias(self) -> None:
        """
        Abre a página 'A vencer em 3 dias' pelo menu inferior.
        """
        self._click(POWERBI_PAGE_MENU)
        self._click(POWERBI_PAGE_A_VENCER)