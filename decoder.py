# class for decoding text from image
from PIL import Image

class Decoder:
    def __init__(self, img:str):
        self.img = img
        self.original_img = Image.open(self.img)
        
        

    def check_png(self) -> bool:
        if self.img.endswith('.png'):
            return True
        return False

    def check_header(self) -> bool:
        ''' check if the first pixel has 0 in its R value '''
        rgb_values = list(self.original_img.getdata())
        if rgb_values[0][0] == 0:
            return True
        return False
    
    def get_r_value(self,gap:int) -> list:
        '''get the first value of the required pixel after every gap in the image and return the list of it'''
        R_values = []
        R_values_with_gap = []
        a = 1
        for pixels in list(self.original_img.getdata()):
            R_values.append(pixels[0])
        while a <= len(list(self.original_img.getdata())):
            R_values_with_gap.append(R_values[a])
            a = a + gap

        return R_values_with_gap
        


