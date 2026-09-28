import time

import pyautogui

from browser import BrowserController
from datetime import datetime, timedelta
from config import (
    MOUSE_PARK_POSITION,
    POWERBI_VIEW_MENU,
    POWERBI_FULLSCREEN_OPTION,
    POWERBI_PAGE_MENU,
    POWERBI_PAGE_PRIORIDADES,
    POWERBI_PAGE_A_VENCER,
    POWERBI_UI_DELAY,
    POWERBI_REFRESH_INTERVAL,
    POWERBI_REFRESH_WAIT
)


class PowerBIController:
    """
    Responsável por controlar o Power BI aberto no Microsoft Edge.
    """

    def __init__(self):
        self.browser = BrowserController()
        self.last_refresh = None

    def open(self) -> None:
        """Traz o Edge com o Power BI para frente."""
        self.browser.focus()

    def _park_mouse(self) -> None:
        """
        Move o cursor para uma posição discreta após as interações.
        """
        x, y = MOUSE_PARK_POSITION
        pyautogui.moveTo(x, y, duration=0.2)

    def _click(self, position: tuple[int, int]) -> None:
        """
        Move o cursor até uma coordenada e realiza um clique.
        """
        x, y = position

        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.click()

        time.sleep(POWERBI_UI_DELAY)

    def needs_refresh(self) -> bool:
        """
        Verifica se já passou o intervalo configurado
        desde o último refresh do Power BI.
        """
        if self.last_refresh is None:
            return True

        elapsed = datetime.now() - self.last_refresh

        return elapsed >= timedelta(seconds=POWERBI_REFRESH_INTERVAL)


    def refresh(self) -> None:
        """
        Recarrega a página atual do Power BI usando Ctrl + R.
        """
        self.browser.focus()

        print("Atualizando Power BI...")

        pyautogui.hotkey("ctrl", "r")

        time.sleep(POWERBI_REFRESH_WAIT)

        self.last_refresh = datetime.now()

        print("Power BI atualizado.")

    def enter_fullscreen(self) -> None:
        """
        Entra no modo tela cheia do Power BI.

        Fluxo:
        1. Abre o menu de exibição.
        2. Clica na opção de tela cheia.
        """
        self._click(POWERBI_VIEW_MENU)
        self._click(POWERBI_FULLSCREEN_OPTION)

        self._park_mouse()

    def exit_fullscreen(self) -> None:
        """Sai do modo tela cheia."""
        pyautogui.press("esc")
        time.sleep(POWERBI_UI_DELAY)

        self._park_mouse()

    def show_prioridades(self) -> None:
        """
        Abre a página 'Prioridades' pelo menu inferior.
        """
        self._click(POWERBI_PAGE_MENU)
        self._click(POWERBI_PAGE_PRIORIDADES)

        self._park_mouse()

    def show_a_vencer_3_dias(self) -> None:
        """
        Abre a página 'A vencer em 3 dias' pelo menu inferior.
        """
        self._click(POWERBI_PAGE_MENU)
        self._click(POWERBI_PAGE_A_VENCER)

        self._park_mouse()