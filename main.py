
from json import load
import time
from tkinter import *
from tkinter.ttk import *
import os
from pynput.keyboard import Controller
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style

clear = os.system("cls" if os.name == "nt" else "clear")
Style.RESET_ALL

while True:
    os.system("cls" if os.name == "nt" else "clear")

    speed_input = input(Fore.LIGHTCYAN_EX +
                        "Typingspeed (1-5): " + Style.RESET_ALL)

    if speed_input == "1":
        speed = 0.01
        break

    if speed_input == "2":
        speed = 0.1
        break

    if speed_input == "3":
        speed = 0.5
        break

    if speed_input == "4":
        speed = 1
        break

    if speed_input == "5":
        speed = 2
        break

    else:

        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "Please use an available option! (1-5)" + Style.RESET_ALL)
        time.sleep(1.5)

str(speed_input)


while True:
    clear = os.system("cls" if os.name == "nt" else "clear")
    print(Fore.LIGHTCYAN_EX + "Typingspeed: " + Style.RESET_ALL + speed_input)
    browserinput = input(Fore.LIGHTCYAN_EX +
                         "Use Chrome or Edge? " + Style.RESET_ALL)

    if browserinput == "Chrome":
        driver = webdriver.Chrome("driver/chromedriver.exe")
        break

    if browserinput == "Edge":
        driver = webdriver.Edge("driver/msedgedriver.exe")
        break

    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.RED + "Please use an available option!" + Style.RESET_ALL)
        time.sleep(1.5)


def main():
    keyboard = Controller()

    os.system("cls" if os.name == "nt" else "clear")

    driver.get("https://at4.typewriter.at/index.php?r=typewriter/runLevel")

    WebDriverWait(driver, 10000).until(EC.url_to_be(
        "https://at4.typewriter.at/index.php?r=user/overview"))

    def typewriter():
        while True:

            time.sleep(1)

            driver.get(
                "https://at4.typewriter.at/index.php?r=typewriter/runLevel")

            keyboard.press("q")
            keyboard.release("q")

            aclet1 = driver.find_element_by_id("actualLetter")
            aclet = aclet1.text

            keyboard.press(aclet)
            keyboard.release(aclet)
            time.sleep(1)

            aclet1 = driver.find_element_by_id("actualLetter")
            aclet = aclet1.text

            keyboard.press(aclet)
            keyboard.release(aclet)
            time.sleep(1)

            rem1 = driver.find_element_by_id("amountRemaining")
            rem = rem1.text

            os.system("cls" if os.name == "nt" else "clear")

            for y in range(int(rem)):
                aclet_ = driver.find_element_by_id("actualLetter")
                aclet = aclet_.text
                keyboard.press(aclet)
                keyboard.release(aclet)
                time.sleep(float(speed))

            os.system("cls" if os.name == "nt" else "clear")

            time.sleep(1)

    typewriter()


main()
