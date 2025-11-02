import pyautogui                            # Used to type something to the user's screen           
import time                                 # To wait for the program to open a text editor window   

def nintendo_intro():                       # Types a message out on the user's machine one character at a time
    message = "NIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINNTENDOOOOOOOOOOOOOOOOOOOOOOOOOOO, WOOOOHOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"   # I had Mario Kart: Double Dash's "Ninteno Intro" playing on the side for reference
    print("Play https://www.youtube.com/watch?v=6-QMdjq6NYY alongside this for a more enjoyable, not weird-looking experience!")


    time.sleep(3)                           # Waits 3 seconds before typing to the selected window
    #TODO: Based on the operating system of the user, open the correct text editor (Windows, Mac, Linux)
    
    pyautogui.typewrite(message, interval=0.03)

if __name__ == "__main__":
    nintendo_intro()