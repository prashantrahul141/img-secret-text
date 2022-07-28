# class for incoding text in image
from PIL import Image
from math import ceil, floor

class Incoder:
    def __init__(self, img:str, text:str, gaps:int) -> None:
        self.img = img
        self.text = text
        self.gaps = gaps
        self.original_img = Image.open(self.img)
        self.convert_png()
    
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
        _total_length = self.IMG.size[0] * self.IMG.sizimage.pnge[1]
        _max_gap = _total_length - 1/ceil(len(self.text)/3)
        return floor(_max_gap)
    

    def incode_header(self) -> None:
        self.IMG.putpixel((0, 0), (0, len(self.text), self.gaps))
        self.IMG.save("output.png")
        
    def incode(self) -> bool:
        self.incode_header()
        
        counter = 0
        index_ = 0
        text_index = 0
        list_of_pixel_values = [(self.gaps*i + 2) for i in range(ceil(len(self.text)/3))[1:]]
        list_of_pixel_values = [2] + list_of_pixel_values

        print(list_of_pixel_values)
        for x in range(self.IMG.size[1]):
            for y in range(self.IMG.size[1]):

                counter += 1
                if x*y == list_of_pixel_values[index_]:
                    index_ += 1

                    # incoding text at x, y
                    # incode

                    if index_ >= len(list_of_pixel_values):
                        return True


    def get_secret_value(self, _index) -> tuple:
        '''will return the secret numeric values of charatcers from the text'''
        pass
