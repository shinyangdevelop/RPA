import pyautogui

img = pyautogui.screenshot()
img.save("screenshot.png")

pixel = pyautogui.pixel(12, 9)
print(pixel)

print(pyautogui.pixelMatchesColor(12, 9, pixel))