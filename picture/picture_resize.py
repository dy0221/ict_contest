import cv2

image_locatiom = ['/home/dy/opencv_study_project/image1.jpeg']

image = cv2.imread(image_locatiom[0])

resize_img = cv2.resize(image, None, fx=0.4, fy=0.4, interpolation=cv2.INTER_AREA)
resize_img = resize_img[300:,:]
# cv2.imshow('resize_image', resize_img)
# cv2.waitKey(0) 
# cv2.destroyAllWindows()
cv2.imwrite('resize_image1.jpeg', resize_img)
