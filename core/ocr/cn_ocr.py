from core.ocr.winocr import recognize_file


class WINOCR_CN:
    def __init__(self):
        pass

    def ocr_for_single_line(self, img):
        return recognize_file(img,'zh-cn')['merged_text']

    def ocr(self, img):
        return recognize_file(img,'zh-cn')
