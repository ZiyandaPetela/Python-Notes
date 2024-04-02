from tkinter import *
from tkinter import ttk

class DailyDigestGUI:
    def __init__(self,root) :
        pass #build the GUI
    """
    The GUI should enable the admin to...
    - configure which content sources to include in email
     add recipients
    -remobe recipients 
    -schedule daily item to send email
    -configure sender credentials
    """
if __name__ == '__main__':
    root=Tk()
    app=DailyDigestGUI(root)
    root.mainloop
