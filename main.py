import webcam.webcam_mesh as webcam_mesh
import picture.picture_mesh as picture_mesh
import picture.picture_text_read as picture_text_read
from face_comparison_thresshold import THRESSHOLD
from add import add

import cv2
import mediapipe as mp
import time
import datetime

while True:
  PICTURE_AVAIALBE = False
  COMPARE_AVAIABLE = False
  BIRTH_AVAIABLE = False
  SAVEINFORMATION_AVAIABLE = False
  BEVERAGE_AVAIABLE = False
  image_location = '/home/dy/opencv_study_project/resize2_image1.jpeg'
  COMPARE_COUNT = 0
  name = 0
  birth = 0
  current_time = 0
  try:
    picture_image = picture_mesh.face_mesh(image_location)
    text = picture_text_read.text_read()
  except:
    print('주민등록증 인식 실패')
    continue
  confirm = input('주민등록확인 다음 절차 진행 [y or n]')
  if confirm == 'y':
    print('다음절차 진행')
    PICTURE_AVAIALBE = True
  else: 
    print('처음으로 돌아갑니다')
  time.sleep(3)

  while PICTURE_AVAIALBE:
    try:
      web_image = webcam_mesh.face_mesh()
      print('얼굴 인식 중')
    except:
      confirm2 = input('얼굴 인식 실패. 처음으로 돌아가기 [y or n]')
      if confirm2 == 'y':
        break
      else :
        continue
    picture_value = add(picture_image)
    web_value = add(web_image)
    face_comparison_weight = (picture_value-web_value)**2
    if face_comparison_weight< THRESSHOLD:
      COMPARE_AVAIABLE = True
      PICTURE_AVAIALBE = False
      print('얼굴 인식 성공')
      time.sleep(3)
      break
    else: 
      COMPARE_COUNT += 1
    
    if COMPARE_COUNT >15 :
      confirm3 = input('다른 얼굴로 판단. 처음으로 돌아가기 [y or n]')
      if confirm3 == 'y':
        time.sleep(3)
        break
      else:
        COMPARE_COUNT = 0
    
  if COMPARE_AVAIABLE:
    name = text['name']
    name = name[:3]
    birth = text['birth']
    birth = birth[:6]
    if int(birth[0])>0 or int(birth[1])<2:
      print('성인 확인')
      COMPARE_AVAIABLE = False
      SAVEINFORMATION_AVAIABLE = True
      time.sleep(3)
    else:
      print('미성년자라고 판단')
      COMPARE_AVAIABLE = False
      pass
      
  if SAVEINFORMATION_AVAIABLE:
    with open('/home/dy/opencv_study_project/information.txt', "r") as f :
      name = f.read()

    current_time = datetime.datetime.now()

    if name is not None:
      name = name[:-2]
      c_time = datetime.datetime.now()
      information_list = name.split(',')
      for information in information_list:
        information_info = information.split("  ")
        f_name = information_info[0]
        f_birth = information_info[1]
        f_time = information_info[3]
        if f_name != name:
          break
        if f_birth != birth:
          break
        #['2023-03-02', '02:29:02.36099']
        f_time_list = f_time.split(" ")
        c_time_list = str(current_time).split(" ")

        f_time_year_list = f_time_list[0].split("-")
        f_time_year = f_time_year_list[0]
        f_time_month = f_time_list[1]
        f_time_day = f_time_list[2]

        c_time_year_list = c_time_list[0].split("-")
        c_time_year = c_time_year_list[0]
        c_time_month = c_time_list[1]
        c_time_day = c_time_list[2]
        if (int(c_time_year)-int(f_time_year))==1:
          if int(c_time_month) == 1 and int(f_time_month)== 12:
            
        if int(c_time_year)==int(f_time_year):

        
        if int(f_time_list[1][3:5]    
  
   
    with open('/home/dy/opencv_study_project/information.txt', "w") as f :
      f.write('{0}  {1}  {2},'.format(name, birth, current_time))
    BEVERAGE_AVAIABLE = True

 


  if cv2.waitKey(5)& 0XFF == 27:
    break 

  