import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu)