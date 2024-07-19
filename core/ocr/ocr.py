import time
import cv2
# from cnocr import CnOcr


class Baas_ocr:
    def __init__(self, logger, ocr_needed=None):
        self.logger = logger
        self.ocrEN = None
        self.ocrCN = None
        self.ocrJP = None
        self.ocrNUM = None
        self.initialized = {
            'CN': False,
            'Global': False,
            'NUM': False,
            'JP': False
        }
        self.init(ocr_needed)

    def init(self, ocr_needed):
        try:
            self.logger.info("ocr needed: " + str(ocr_needed))
            if 'NUM' in ocr_needed:
                self.init_NUMocr()
            if 'CN' in ocr_needed:
                self.init_CNocr()
            if 'Global' in ocr_needed:
                self.init_ENocr()
            if 'JP' in ocr_needed:
                self.init_JPocr()
        except Exception as e:
            self.logger.error("OCR init error: " + str(e))
            raise e

    def init_ENocr(self):
        if self.ocrEN is None:
            from core.ocr.en_ocr import WINOCR_EN
            self.ocrEN = WINOCR_EN()
            img_EN = cv2.imread('src/test_ocr/EN.png')
            self.logger.info("Test ocrEN : " + self.ocrEN.ocr_for_single_line(img_EN)['merged_text'])
        return True

    def init_CNocr(self):
        if self.ocrCN is None:
            from core.ocr.cn_ocr import WINOCR_CN
            self.ocrCN = WINOCR_CN()
            img_CN = cv2.imread('src/test_ocr/CN.png')
            self.logger.info("Test ocrCN : " + self.ocrCN.ocr_for_single_line(img_CN)['merged_text'])
        return True

    def init_NUMocr(self):
        if self.ocrNUM is None:
            from core.ocr.cn_ocr import WINOCR_CN
            self.ocrNUM = WINOCR_CN()
            img_NUM = cv2.imread('src/test_ocr/NUM.png')
            self.logger.info("Test ocrNUM : " + self.ocrNUM.ocr_for_single_line(img_NUM)['merged_text'])
        return True

    def init_JPocr(self):
        if self.ocrJP is None:
            from core.ocr.jp_ocr import PPOCR_JP
            self.ocrJP = PPOCR_JP()
            img_JP = cv2.imread('src/test_ocr/JP.png')
            self.logger.info("Test ocrJP : " + self.ocrJP.ocr_for_single_line(img_JP)['text'])

    def get_region_num(self, img, region, category=int, ratio=1.0):
        img = self.get_region_img(img, region, ratio)
        res = self.ocrNUM.ocr_for_single_line(img)['text']
        res = res.replace('<unused3>', '')
        res = res.replace('<unused2>', '')
        temp = ''
        for i in range(0, len(res)):
            if res[i].isdigit():
                temp += res[i]
            elif res[i] == '.' and category == float:
                temp += res[i]

        if temp == '':
            return "UNKNOWN"
        return category(temp)

    def get_region_pure_english(self, img, region, ratio=1.0):
        img = self.get_region_img(img, region, ratio)
        res = self.ocrEN.ocr_for_single_line(img)['text']
        res = res.replace('<unused3>', '')
        res = res.replace('<unused2>', '')
        temp = ''
        for i in range(0, len(res)):
            if self.is_english(res[i]):
                temp += res[i]
        return temp

    def get_region_pure_chinese(self, img, region, ratio=1.0):
        img = self.get_region_img(img, region, ratio)
        res = self.ocrCN.ocr_for_single_line(img)['text']
        res = res.replace('<unused3>', '')
        res = res.replace('<unused2>', '')
        temp = ''
        for i in range(0, len(res)):
            if self.is_chinese_char(res[i]):
                temp += res[i]
        return temp

    def is_upper_english(self, char):
        if 'A' <= char <= 'Z':
            return True
        return False

    def is_lower_english(self, char):
        if 'a' <= char <= 'z':
            return True
        return False

    def is_english(self, char):
        return self.is_upper_english(char) or self.is_lower_english(char)

    def is_chinese_char(self, char):
        return 0x4e00 <= ord(char) <= 0x9fff

    def get_region_res(self, img, region, model='CN', ratio=1.0):
        img = self.get_region_img(img, region, ratio)
        res = ""
        if model == 'CN':
            res = self.ocrCN.ocr_for_single_line(img)['text']
        elif model == 'Global':
            res = self.ocrEN.ocr_for_single_line(img)['text']
        elif model == 'NUM':
            res = self.ocrNUM.ocr_for_single_line(img)['text']
        elif model == 'JP':
            res = self.ocrJP.ocr_for_single_line(img)['text']
        res = res.replace('<unused3>', '')
        res = res.replace('<unused2>', '')
        return res

    def get_region_raw_res(self, img, region, model='CN', ratio=1.0):
        img = self.get_region_img(img, region, ratio)
        res = ""
        if model == 'CN':
            res = self.ocrCN.ocr(img)
        elif model == 'Global':
            res = self.ocrEN.ocr(img)
        elif model == 'NUM':
            res = self.ocrNUM.ocr(img)
        elif model == 'JP':
            res = self.ocrJP.ocr(img)
        for i in range(0, len(res)):
            res[i]['text'] = res[i]['text'].replace('<unused3>', '')
            res[i]['text'] = res[i]['text'].replace('<unused2>', '')
        return res

    def get_region_img(self, img, region, ratio=1.0):
        img = img[int(region[1] * ratio):int(region[3] * ratio), int(region[0] * ratio):int(region[2] * ratio)]
        return img
