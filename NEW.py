from pynput.keyboard import Key, Controller

from win32api import GetKeyState 
from win32con import VK_CAPITAL 
print(GetKeyState(VK_CAPITAL))