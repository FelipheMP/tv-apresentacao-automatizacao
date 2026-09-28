import time

import pyautogui
import win32con
import win32gui

from window_utils import force_foreground


class BrowserController:
    """
    Responsável por localizar e ativar a janela do Microsoft Edge.

    Usa diretamente a API Win32, evitando problemas do pygetwindow
    ao tentar ativar janelas.
    """

    def __init__(self, title_keyword: str = "Edge"):
        self.title_keyword = title_keyword.lower()

    def is_available(self) -> bool:
        """
        Verifica se existe uma janela do Edge disponível.
        """
        try:
            self._find_window()
            return True
        except RuntimeError:
            return False

    def _find_window(self) -> int:
        """
        Procura uma janela visível do Microsoft Edge.

        Retorna o HWND da primeira janela encontrada.
        """

        found_windows = []

        def enum_callback(hwnd, _):
            if not win32gui.IsWindowVisible(hwnd):
                return

            title = win32gui.GetWindowText(hwnd)

            if not title:
                return

            if self.title_keyword in title.lower():
                found_windows.append(hwnd)

        win32gui.EnumWindows(enum_callback, None)

        if not found_windows:
            raise RuntimeError(
                f"Nenhuma janela contendo "
                f"'{self.title_keyword}' foi encontrada."
            )

        return found_windows[0]

    def focus(self) -> None:
        """
        Traz a janela do Edge para o primeiro plano.
        """
        hwnd = self._find_window()
        force_foreground(hwnd)

    def open_address(self, url: str) -> None:
        """
        Abre uma URL na aba atual do Edge.
        """

        self.focus()

        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.2)

        pyautogui.write(url, interval=0.001)
        pyautogui.press("enter")