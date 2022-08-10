# class for decoding text from image
from PIL import Image

class Decoder:
    def __init__(self, img:str, secret_list:list):
        self.img = img
        self.IMG = Image.open(self.img)
        self.secret_list = secret_list

        if not self.check_png():
            raise TypeError("File not incoded.")
            del self

        self.image_array_data = list(self.IMG.getdata())
        self.image_header = self.get_header()

        if not self.check_header():
            raise TypeError("File not incoded.")
            del self


    def check_png(self) -> bool:
        '''checks if the image is png or not'''
        if self.img.endswith('.png'):
            return True
        return False


    def get_header(self) -> list:
        '''rturns the header value in form of [length, gap]'''
        _first_pixel = list(self.image_array_data)[0]
        return [_first_pixel[0], _first_pixel[1], _first_pixel[2]]


    def check_header(self) -> bool:
        ''' check if the first pixel has 0 in its R value '''
        if self.image_header[0] == 0:
            return True
        False
    

    def decode(self) -> str:
        '''returns actual text stored'''

        list_of_r_values = []
        _counter_for_text_length = 0
        for i in range(1, len(self.image_array_data), self.image_header[2]-1):
            list_of_r_values.append(self.image_array_data[i][0])
            if _counter_for_text_length >= self.image_header[1]-1:
                break
            _counter_for_text_length += 1
        return self.convert_to_secret_text(list_of_r_values)
    
    def convert_to_secret_text(self, _list:list) -> str:
        '''converts indexs to secret text value in one string'''
        _string = ""
        for i in _list:
            if 0 <= i < len(self.secret_list):
                _string += self.secret_list[i]
            else:
                _string += "~"
        return _string



import json
with open("secret_text_list.json", 'r') as f:
    data = json.load(f)["list"]
        
decode = Decoder("output.png", data)
print(decode.decode())