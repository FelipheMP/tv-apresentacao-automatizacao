import time

import pyautogui


print("Posicione o mouse sobre o elemento desejado.")
print("Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"\rX: {x:4} | Y: {y:4}", end="")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nEncerrado.")