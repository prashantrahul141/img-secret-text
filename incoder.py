# class for incoding text in image
from PIL import Image
from math import ceil, floor

class Incoder:
    def __init__(self, img_name:str, text:str, secret_list:list, gaps:int = 0) -> None:
        self.img_name = img_name
        self.text = text
        self.secret_list = secret_list
        self.convert_img()
        self.gaps = self.max_gap() if gaps == 0 else gaps
        self.image_array_data = self.IMG.getdata()
        print(self.gaps)
    
    def convert_img(self):
        '''converts jpg img into png to avoid jpg compression'''
        _original_img = Image.open(self.img_name)
        _original_img.save("output.png")
        self.IMG = Image.open("output.png")
   
    def check_length(self):
        '''checks if the given value is under max gap'''
        if self.gaps < self.max_gap():
            return True
        return False


    def max_gap(self) -> bool:
        '''returns the max gap which is possible '''
        _total_length = self.IMG.size[0] * self.IMG.size[1]
        _max_gap = _total_length/len(self.text)
        return floor(_max_gap)
    

    def incode_header(self) -> None:
        self.IMG.putpixel((0, 0), (0, len(self.text), self.gaps))
        self.IMG.save("output.png")

    def incode(self) -> bool:
        '''changes pixel r value according to secret text'''
        self.incode_header()

        list_of_pixel_indexes = []
        _counter_for_text_length = 0

        for i in range(1, len(self.image_array_data), self.gaps):
            list_of_pixel_indexes.append(i)
            if _counter_for_text_length >= len(self.text)-1:
                break;
            _counter_for_text_length += 1

        _counter = 0
        _index = 0

        for y in range(self.IMG.size[1]+1):
            for x in range(self.IMG.size[0]+1):

                if _counter == list_of_pixel_indexes[_index]:
                    self.IMG.putpixel((x, y), self.get_secret_value(_index, _counter))
                    self.IMG.save("output.png")

                    _index += 1
                    if _index >= len(list_of_pixel_indexes):  
                        return True

                _counter += 1
    

    def get_secret_value(self, _index, _counter) -> tuple:
        '''will return the secret numeric values of charatcers from the text'''

        _text = self.text[_index]
        if _text in self.secret_list:
            _r = self.secret_list.index(_text)
            _data = list(self.image_array_data)[_counter]
            _g, _b = _data[1], _data[2];
            return (_r, _g, _b, 255)
           
        raise ValueError(f"character '{_text}' not in secret list.")


import json
with open("secret_text_list.json", 'r') as f:
    data = json.load(f)["list"]

incoder = Incoder("test.png", "hellow", data)
incoder.incode()
for i in list(incoder.IMG.getdata()):
    print(i)
