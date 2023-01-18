import pyautogui
screenWidth, screenHeight = pyautogui.size()
print("Ekran Çzözünürlüğü :", screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

