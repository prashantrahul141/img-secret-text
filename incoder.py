# class for incoding text in image
from PIL import Image
from math import floor

class Incoder:
    def __init__(self) -> None:
        self.img = ""
        self.text = ""
        self.gaps = ""


    def set_img_text_gaps(self, img:str, text:str, gaps:int) -> None:
        '''sets img text and gaps given by user'''
        self.img = img
        self.IMG = Image.open(self.img)
        self.text = text
        self.gaps = gaps


    def check_length(self):
        '''checks if the given value is under max gap'''
        if self.gaps < self.max_gap():
            return True
        return False


    def max_gap(self) -> bool:
        '''returns the max gap which is possible '''

        _total_length = self.IMG.size[0] * self.IMG.size[1]
        return floor((_total_length - 1)/len(self.text))
    

    def incode_header(self) -> bool:
        pass

    def incode(self) -> bool:
        pass


