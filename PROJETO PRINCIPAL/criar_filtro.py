import pyautogui
import pyperclip

# Cria um filtro no sistema com as matriculas passadas, usando o PyAutoGUI

# Create a filter in the system with past registrations, using PyAutoGUI


CAMINHO_ARQUIVO = r"caminho arquivo"

pyautogui.click(611,876, duration=0.8)
pyautogui.click(771,786, duration=0.8)

pyautogui.click(568,485, duration=0.8)

with open("matriculas.txt", "r") as mt:
    for i in mt:
        pyperclip.copy(i)
        pyautogui.doubleClick(885,268, duration=0.5)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.click(1019,339)