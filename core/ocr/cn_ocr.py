from core.ocr.winocr import recognize_file, recognize_pil_image
from PIL import Image;
import cv2


class WINOCR_CN:
    def __init__(self):
        pass

    def ocr_for_single_line(self, img):
        img = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        return recognize_pil_image(img,'zh-cn')

    def ocr(self, img):
        return recognize_file(img,'zh-cn')
