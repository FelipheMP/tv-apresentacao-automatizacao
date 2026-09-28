import time

import win32com.client
import win32con
import win32gui

from config import SLIDE_DURATION, SLIDES_DYNAMIC_POWERBI_PAGES
from window_utils import force_foreground


class PowerPointController:
    """
    Controla a apresentação do PowerPoint.

    Usa COM para controlar os slides e Win32 para localizar
    e trazer a janela fullscreen da apresentação para frente.
    """

    def __init__(self, slide_duration: int = SLIDE_DURATION):
        self.slide_duration = slide_duration

    def _get_application(self):
        try:
            return win32com.client.GetActiveObject(
                "PowerPoint.Application"
            )
        except Exception as exc:
            raise RuntimeError(
                "Não foi possível encontrar uma instância aberta "
                "do PowerPoint."
            ) from exc

    def _get_slideshow(self):
        app = self._get_application()

        if app.SlideShowWindows.Count == 0:
            raise RuntimeError(
                "O PowerPoint está aberto, mas nenhuma apresentação "
                "está em modo de apresentação."
            )

        return app.SlideShowWindows(1)

    def _find_slideshow_window(self):
        """
        Localiza a janela fullscreen da apresentação do PowerPoint.

        A janela de Slide Show utiliza a classe 'screenClass'.
        """
        found_windows = []

        def enum_callback(hwnd, _):
            if not win32gui.IsWindowVisible(hwnd):
                return

            class_name = win32gui.GetClassName(hwnd)

            if class_name == "screenClass":
                found_windows.append(hwnd)

        win32gui.EnumWindows(enum_callback, None)

        if not found_windows:
            raise RuntimeError(
                "Não foi possível localizar a janela fullscreen "
                "da apresentação do PowerPoint."
            )

        return found_windows[0]

    def get_slide_count(self) -> int:
        """
        Retorna a quantidade total de slides da apresentação atual.
        """
        slideshow = self._get_slideshow()

        return slideshow.Presentation.Slides.Count - SLIDES_DYNAMIC_POWERBI_PAGES # Menos os slides dos dashboards do Power BI


    def show_all_slides(self) -> None:
        """
        Exibe todos os slides da apresentação, começando pelo primeiro.
        """
        self.focus()
        self.first_slide()

        total_slides = self.get_slide_count()

        print(f"Apresentação possui {total_slides} slides.")

        for slide_number in range(1, total_slides + 1):
            print(f"Exibindo slide {slide_number}/{total_slides}")

            self.wait()

            if slide_number < total_slides:
                self.next_slide()

    def focus(self) -> None:
        """
        Traz a apresentação fullscreen para frente.
        """
        # Garante que o PowerPoint reconheça a apresentação ativa.
        slideshow = self._get_slideshow()

        slideshow.Activate()

        hwnd = self._find_slideshow_window()

        force_foreground(hwnd)

        time.sleep(1)

    def next_slide(self) -> None:
        slideshow = self._get_slideshow()
        slideshow.View.Next()

    def previous_slide(self) -> None:
        slideshow = self._get_slideshow()
        slideshow.View.Previous()

    def first_slide(self) -> None:
        slideshow = self._get_slideshow()
        slideshow.View.First()

    def wait(self) -> None:
        time.sleep(self.slide_duration)

    def show_slides(self, amount: int) -> None:
        self.focus()

        for slide_number in range(1, amount + 1):
            print(f"Exibindo slide {slide_number}/{amount}")

            self.wait()

            if slide_number < amount:
                self.next_slide()