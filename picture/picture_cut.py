import cv2

import numpy as np
"""
https://www.youtube.com/watch?v=XK3eU9egll8
text1[(162, 386), (350, 381), (352, 450), (159, 456)]
"""

point_list = []
image_location = ['/home/dy/opencv_study_project/resize_image1.jpeg']
image = cv2.imread(image_location[0])

RED = (0,255,0)
THICKNESS =3
drawing = False

def mouse_handler(event, x , y, flags, param):
  global drawing
  cpimage = image.copy()
  write_image = image.copy()
  if event == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    point_list.append((x,y))
  
  if drawing:
    pre_point = None
    for point in point_list:
      cv2.circle(cpimage, point, 15, RED, cv2.FILLED)
      if pre_point:
        cv2.line(cpimage, pre_point, point, RED, THICKNESS, cv2.LINE_AA)
      pre_point = point
    next_point = (x,y)
    if len(point_list) == 4:
      show_result(write_image)
      next_point = point_list[0]
    cv2.line(cpimage,pre_point, next_point, RED, THICKNESS, cv2.LINE_AA)
  cv2.imshow('img',cpimage)

def show_result(image):
  f_x, f_y = point_list[0]
  s_x, s_y = point_list[1]
  t_x, t_y = point_list[2]
  fo_x, fo_y = point_list[3]
  image = image[f_y:fo_y,f_x:s_x]
  cv2.imwrite('resize_text2.jpeg', image)

if __name__ == '__main__':
    cv2.namedWindow('img')
    cv2.setMouseCallback('img', mouse_handler)
    cv2.imshow('img', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print(point_list) 

      