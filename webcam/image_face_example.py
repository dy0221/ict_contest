import cv2
import mediapipe as mp
import webcam.webcam_package.face_draw as face_draw
import webcam.webcam_package.face_connections as face_connections
import webcam.webcam_package.face_triangle_connection as face_triangle_connection

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_face_mesh = mp.solutions.face_mesh
"""
LEFTIRIS = [i for i in range(474,477+1)]
RIGHTIRIS = [i for i in range(469, 472+1)]
LEFTEYE = [263, 249, 390, 373, 374, 380, 381, 382, 362, 466, 388, 387, 386, 385, 384, 398]
RIGHTEYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 246, 161, 160, 159, 158, 157, 173]
LEFTEYEBROW = [276, 283, 282, 295, 285, 300, 293, 334, 296, 336]
RIGHTEYEBROW = [46, 53, 52, 65, 55, 70, 63, 105, 66, 107]
NOSE = [1 ,4 ,5 ,195 ,197 ,6 ,168, 219, 115, 220, 45 , 275, 440, 344, 278]
"""
BLUECOLOR = (255,0,0)
THICKNESS = 3

# For static images:
IMAGE_FILES = ['/home/dy/opencv_study/cut5.png']
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
with mp_face_mesh.FaceMesh(
    static_image_mode=True,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5) as face_mesh:
  for idx, file in enumerate(IMAGE_FILES):
    image = cv2.imread(file)
    image_rows, image_cols, _ = image.shape
    # Convert the BGR image to RGB before processing.
    results = face_mesh.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print and draw face mesh landmarks on the image.
    if not results.multi_face_landmarks:
      continue
    annotated_image = image.copy()
    for face_landmarks in results.multi_face_landmarks:
      landmark_dict = {}
      for idx, landmark in enumerate(face_landmarks.landmark):
        landmark_dict[idx] = face_draw.normalized_to_pixel_coordinates(landmark.x, landmark.y ,  image_cols, image_rows)
      # for idx in face_connections.LEFTIRIS:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
      # for idx in face_connections.RIGHTIRIS:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
      # for idx in face_connections.LEFTEYE:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
      # for idx in face_connections.RIGHTEYE:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA) 
      # for idx in face_connections.LEFTEYEBROW:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
      # for idx in face_connections.RIGHTEYEBROW:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
      # for idx in face_connections.NOSE:
      #   cv2.putText(annotated_image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA) 

      left_eye_area = face_draw.sum_area(landmark_dict, face_connections.LEFTEYEAREA)
      left_iris_length = face_draw.sum_line(landmark_dict, [(476,474)])
      left_eye_length = face_draw.sum_line(landmark_dict, [(362,363)])
      left_iris_area = face_draw.sum_area(landmark_dict,face_connections.LEFTIRISAREA)
      left_eyelength_ratio = (left_eye_length/left_iris_length)
      left_eyearea_ratio = (left_eye_area/left_iris_area)

      right_eye_area = face_draw.sum_area(landmark_dict, face_connections.RIGHTEYEAREA)
      right_iris_length = face_draw.sum_line(landmark_dict, [(471,469)])
      right_eye_length = face_draw.sum_line(landmark_dict, [(33,133)])
      right_iris_area = face_draw.sum_area(landmark_dict,face_connections.RIGHTIRISAREA)
      right_eyelength_ratio = (right_eye_length/right_iris_length)
      right_eyearea_ratio = (right_eye_area/right_iris_area)        

      nose_bridge_length = face_draw.sum_line(landmark_dict, face_connections.NOSEBRIDGELINE)
      nose_horizon_length = face_draw.sum_line(landmark_dict, face_connections.NOSEHORIZONLINE)

      nose_length_ratio = (nose_bridge_length/nose_horizon_length)

      left_eyebrowup_length = face_draw.sum_line(landmark_dict, face_connections.LEFTEYEBROWUP)
      left_eyebrowdown_length = face_draw.sum_line(landmark_dict, face_connections.LEFTEYEBROWDOWN)

      right_eyebrowup_length = face_draw.sum_line(landmark_dict, face_connections.RIGHTEYEBROWUP)
      right_eyebrowdown_length = face_draw.sum_line(landmark_dict, face_connections.RIGHTEYEBROWDOWN)

      left_eyebrow_ratio = (left_eyebrowup_length/left_eyebrowdown_length)
      right_eyebrow_ratio = (right_eyebrowup_length/right_eyebrowdown_length)
      
      face_area = face_draw.sum_area(landmark_dict, face_triangle_connection.triangle_conection)
      face_area_ratio = face_area/(left_eye_area+right_eye_area+(nose_bridge_length*nose_horizon_length))
      print(face_area_ratio)       
      # print("left_area : {0}, left_length : {1}".format(left_eyearea_ratio,left_eyelength_ratio))
      # print("right_area : {0}, right_length : {1}".format(right_eyearea_ratio,right_eyelength_ratio))
      # print('nose_length : {0}'.format(nose_length_ratio))
      # print('left_eyebrow : {0}, right_eyebrow :{1}'.format(left_eyebrow_ratio,right_eyebrow_ratio))
    cv2.imshow("annoted_image", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()           
    
#copy 0.3392857142857143
  