# class for incoding text in image
from PIL import Image
from math import ceil, floor

class Incoder:
    def __init__(self, img:str, text:str, secret_list:list, gaps:int = 0) -> None:
        self.img = img
        self.text = text
        self.secret_list = secret_list
        self.original_img = Image.open(self.img)
        self.convert_png()
        self.gaps = self.max_gap() if gaps == 0 else gaps
    
    def convert_png(self):
        self.original_img.save("output.png")
        self.IMG = Image.open("output.png")


    def check_length(self):
        '''checks if the given value is under max gap'''
        if self.gaps < self.max_gap():
            return True
        return False


    def max_gap(self) -> bool:
        '''returns the max gap which is possible '''
        _total_length = self.IMG.size[0] * self.IMG.size[1]
        _max_gap = _total_length - 1/ceil(len(self.text))
        return floor(_max_gap)
    

    def incode_header(self) -> None:
        self.IMG.putpixel((0, 0), (0, len(self.text), self.gaps))
        self.IMG.save("output.png")
        
    def incode(self) -> bool:
        self.incode_header()
        
        counter = 0
        _index = 0
        list_of_pixel_values = [(self.gaps*i + 2) for i in range(ceil(len(self.text)))[1:]]
        list_of_pixel_values = [2] + list_of_pixel_values

        for x in range(self.IMG.size[1]):
            for y in range(self.IMG.size[1]):

                counter += 1
                if x*y == list_of_pixel_values[_index]:
                    _index += 1

                    # incoding text at x, y
                    self.IMG.putpixel((x, y), self.get_secret_value(_index))
                    if _index >= len(list_of_pixel_values):
                        return True


    def get_secret_value(self, _index) -> tuple:
        '''will return the secret numeric values of charatcers from the text'''

        _text = self.text[_index]
        if _text in self.secret_list:
            return self.secret_list.index(_text)
        raise ValueError(f"character '{_text}' not in secret list.")
        


import json
with open("secret_text_list.json", 'r') as f:
    data = json.load(f)["list"]


incoder = Incoder("text_image.jpg", "hellow", data)
incoder.incode()