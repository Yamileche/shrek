import pyautogui
import time

if __name__ == "__main__":
    with open("shrek.txt", "r") as shrek:
        for line in shrek:
            if line !="\n":
                line  = line.replace("\n", "")
                time.sleep(0.5)
                pyautogui.typewrite(line)
                pyautogui.press("enter")
 