# string = 'The quick brown fox jusmps over the lazy dog'
# # Define your variables
# result = ''
# for i in string:
#         if i == 'o':
#                 i = '0'
#         result += i
# print(result)


from pynput.keyboard import Key, Controller

from win32api import GetKeyState 
from win32con import VK_CAPITAL 

keyboard = Controller()
this = 'bcdefghijklmnopqrstuvwxyzBCDEFGHIJKLMNOPQRSTUVWXYZ '


def caps_lock_stuck(text):
    if GetKeyState(VK_CAPITAL) == 1:
        keyboard.press(Key.caps_lock)
    for i in text:
        if i in this:
            keyboard.type(i)
        else:
            keyboard.press(Key.caps_lock)
            keyboard.release(Key.caps_lock)
     
caps_lock_stuck("Why are you asking me that day?")