import cv2

from pytesseract import *

def text_read():
  image_loaction = [('name','/home/dy/opencv_study_project/resize_text1.jpeg'),
                  ('birth','/home/dy/opencv_study_project/resize_text2.jpeg')]
  text_dict = {}
  for key, location in image_loaction:          
    image  = cv2.imread(location)            
    text = pytesseract.image_to_string(image,lang='kor') #한글은 'kor'
    text_dict[key] = text
  return text_dict

if __name__ == '__main__':
  text = text_read()
  name = text['name']
  name = name[:3]
  birth = text['birth']
  birth = birth[:6]
  print(birth) 
  