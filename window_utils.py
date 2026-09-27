import time

import win32con
import win32gui
import win32process
import win32api


def force_foreground(hwnd: int) -> None:
    """
    Traz uma janela para o primeiro plano de forma mais confiável.

    Usa AttachThreadInput para contornar as restrições de foco
    impostas pelo Windows.
    """

    if not win32gui.IsWindow(hwnd):
        raise RuntimeError("HWND inválido.")

    if win32gui.IsIconic(hwnd):
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

    foreground_hwnd = win32gui.GetForegroundWindow()

    current_thread_id = win32api.GetCurrentThreadId()

    foreground_thread_id, _ = win32process.GetWindowThreadProcessId(
        foreground_hwnd
    )

    target_thread_id, _ = win32process.GetWindowThreadProcessId(
        hwnd
    )

    attached_foreground = False
    attached_target = False

    try:
        if foreground_thread_id != current_thread_id:
            win32process.AttachThreadInput(
                current_thread_id,
                foreground_thread_id,
                True
            )
            attached_foreground = True

        if target_thread_id != current_thread_id:
            win32process.AttachThreadInput(
                current_thread_id,
                target_thread_id,
                True
            )
            attached_target = True

        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.BringWindowToTop(hwnd)
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SetFocus(hwnd)

    finally:
        if attached_target:
            win32process.AttachThreadInput(
                current_thread_id,
                target_thread_id,
                False
            )

        if attached_foreground:
            win32process.AttachThreadInput(
                current_thread_id,
                foreground_thread_id,
                False
            )

    time.sleep(0.5)