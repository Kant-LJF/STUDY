#!/user/bin/env python
# _*_coding=utf-8_*_

import cv2
import pytesseract

def recognize_captcha(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    captcha_text = pytesseract.image_to_string(gray)
    return captcha_text

if __name__ == '__main__':
    captcha_text = recognize_captcha('captcha.jpg')
    print('验证码识别结果：', captcha_text)
