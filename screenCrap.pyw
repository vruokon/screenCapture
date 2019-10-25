import glob, os
from pynput.mouse import Listener
from PIL import Image, ImageGrab



class screenShot(object):
    
    def __init__(self):
        self.coordinate = []
    
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
            img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
            img.save('shot.png')
            
            

    

    

screen = screenShot()
screen.listen()
