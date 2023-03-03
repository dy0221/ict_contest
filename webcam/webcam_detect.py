
import cv2
import mediapipe as mp


# For webcam input:
def webcam_detect() ->list:
  try:
    cap = cv2.VideoCapture(0)
  except:
    return
  mp_face_detection = mp.solutions.face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.8)
  
  success, image = cap.read()
  if not success:
    print("Ignoring empty camera frame.")
    cap.release()
    return
  image_rows, image_cols, _ = image.shape 
  image.flags.writeable = False

  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  results = mp_face_detection.process(image)

  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

  cp_image = image.copy()
  if not results.detections:
    cap.release()
    return
  for detection in results.detections:
    bounding_box = detection.location_data.relative_bounding_box
    x, y, w, h = int(bounding_box.xmin * image_cols),\
                 int(bounding_box.ymin * image_rows),\
                 int(bounding_box.width * image_cols),\
                 int(bounding_box.height * image_rows)
  if(0<x and x<image_cols and 0<y and y<image_rows):
    cp_image = cp_image[y:y+h, x:x+w]
    cap.release()
    return cp_image
  else:
    cap.release()
    return    

if __name__ =='__main__':
  while True:
    image = webcam_detect()
    print(image)
    cv2.imshow('11',image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
  
  

