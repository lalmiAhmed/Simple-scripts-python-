import pyautogui
import time 


order = 0
delay = 0.4
rng = int(input(" enter the number of files ...  "))


print("you have 5 seconds to focus on the specified dir ...\n")
time.sleep(5);

pyautogui.press('Home')
for i in range(0,rng) :
    order +=1    
    pyautogui.press('f2')
    pyautogui.write("pic")
    pyautogui.press('Home')    
    pyautogui.keyDown('shift')
    pyautogui.write("0" + str(order))
    pyautogui.keyUp('shift')
    pyautogui.write("-")
    pyautogui.press('enter')
    time.sleep(0.5)    
    pyautogui.press('down')    
    time.sleep(delay)

print("work done !")
print(order)



o
