import glob, os
from pynput.mouse import Listener
from PIL import Image, ImageGrab
from datetime import datetime as dt



class screenShot(object):
    
    def __init__(self):
        self.coordinate = []
        self.name = dt.now().strftime("%d-%m-%y-%H-%M-%S")
    
    def listen(self):
        with Listener(on_click=self.on_click) as self.listener:
            self.listener.join()

    def on_click(self, x, y, button, pressed):
        if(pressed):
            self.coordinate.append(x)
            self.coordinate.append(y)
            self.checkLen()

    def checkLen(self):
        if(len(self.coordinate) > 3):
            self.listener.stop()
            x1 = self.coordinate[0]
            y1 = self.coordinate[1]
            x2 = self.coordinate[2]
            y2 = self.coordinate[3]
            
            if(x1>x2):
                tmp = x2
                x2 = x1
                x1 = tmp
            if(y1>y2):
                tmp = y2
                y2 = y1
                y1 = tmp

            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            img.save(self.name + ".png")
            
            


screen = screenShot()
screen.listen()
