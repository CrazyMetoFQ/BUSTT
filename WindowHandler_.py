"""
I litteraly want to kms after the amount of work I had to do just for this
GL
"""

import win32gui
import win32con
import win32api



class Wnd:

    def __init__(self, title) -> None:
        self.title = title
        self.hwnd = win32gui.FindWindow(0,title)

    def set_keys(self,keys:list) -> None:
        """
        keys will be the Hex codes
        Use this for speciial keys such as fn
        """
        # VK_ = 0x74 # Desired virtual key code | google this
        # hwcode = win32api.MapVirtualKey(VK_, 0)

        self.kh_l = [(VK_, win32api.MapVirtualKey(VK_, 0)) for VK_ in keys]

    def send_keys(self):
        """
        sends keys set from set_keys
        """
        for VK_,hwcode in self.kh_l:
            win32api.keybd_event(VK_, hwcode)

    def close_window(self):
        """
        Closes Window
        """
        win32gui.PostMessage(self.hwnd,win32con.WM_CLOSE,0,0)

    def set_post(self):
        """
        Edit this to use send post method
        WARNING: USE PYWIN32 (pain)
        """
        return None # return (keytype, hexcode, 0)
    
    def send_post(self):
        """
        sends msg set from set_post
        """
        if self.set_post()!=None:
            pass
        else:
            print("Idiot")

        
    
