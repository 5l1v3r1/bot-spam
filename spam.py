import pyautogui, time

time.sleep(5)


x = open("text", "r")

for word in x:
    pyautogui.typewrite(word)
    pyautogui.press("Enter")

