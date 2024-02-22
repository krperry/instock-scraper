"""A version of instock that uses threads and WX to make a GUI"""

#See readme for module install instructions.
import threading
import requests
import time
from bs4 import BeautifulSoup
import wx


class UrlRequester(threading.Thread):
    """A thread class that runs for each item"""

    def __init__(self, name, url):
        """The constructor for the thread class"""
        threading.Thread.__init__(self)
        self.name = name
        self.url = url
        self.line = ""

    def run(self):
        """The heart of the thread class that does the work"""
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, "html.parser")
        in_stock = soup.find_all("p", class_="stock")[0].get_text()
        self.line = f"{self.name}: {in_stock}\n"


class Mywin(wx.Frame):
    """This is a frame from WX used to make the simple dialog"""

    def __init__(self, parent, title):
        """The class constructor with the Text field"""
        
        #super calls the base wx class constructor 
        super(Mywin, self).__init__(parent, title=title, size=(350, 300))

        #This is a window that will hold the box  sizer  control
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        #The text control that will hold the items
        self.text = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        self.text.AppendText("Loading product information...")

        #All the products like in the other loop function
        self.products = [
            ("https://www.aph.org/product/mantis-q40/", "Mantis"),
            ("https://www.aph.org/product/chameleon-20/", "Chameleon"),
            ("https://www.aph.org/product/pixblaster/", "PixBlaster"),
            ("https://www.aph.org/product/pageblaster/", "PageBlaster"),
            (
                "https://www.aph.org/product/mantis-q40-executive-leather-case/",
                "Mantis Case",
            ),
            (
                "https://www.aph.org/product/digital-talking-book-cartridge/",
                "Green Talking Book Cart",
            ),
            ("https://www.aph.org/product/sunu-band/", "Sunu Band"),
        ]

        #add the text control to the box sizer
        box.Add(self.text, 1, wx.EXPAND)


        # add the box sizer to to the control panel
        panel.SetSizer(box)
        panel.Fit()

        #center the panel on the window s area
        self.Centre()

        # show the frame
        self.Show(True)

        # run the loader. defined in this class below
        self.loadProductInfo()

    def loadProductInfo(self):
        """function that runs the thread task class to load all the items """
        tasks = []
        for url in self.products:
            tasks.append(UrlRequester(url[1], url[0]))
        for t in tasks:
            t.start()
        for t in tasks:
            t.join()
        self.text.Clear()
        for t in tasks:
            self.text.AppendText(t.line)


ex = wx.App()
Mywin(None, "Quick product stock")
ex.MainLoop()
