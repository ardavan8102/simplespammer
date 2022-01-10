import pyautogui, time, keyboard

#  Place Everything In While Loop
while True:
    try:
        if keyboard.is_pressed('backspace'): # Activate Proccess WIth Pressing Backspace Button
            while True:
                time.sleep(1) # Wait Before Sending Message Again (Recommend 1 Sec)
                words = open(r"") # Place The Text File Location in rString
                
                # Send Every Sentence In Text File
                for word in words:
                    pyautogui.typewrite(word)
                    pyautogui.press('enter')
    except:
        print('Error')