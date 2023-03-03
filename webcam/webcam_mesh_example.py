import cv2
import mediapipe as mp
from webcam_package import face_draw
from webcam_package import face_connections
from dataclasses import dataclass
from webcam_package import face_triangle_connection

@dataclass
class picture_weight:
  left_eye_len_ratio : float
  left_eye_area_ratio : float 
  left_eyebrow_len_ratio : float 
  right_eye_len_ratio : float 
  right_eye_area_ratio : float 
  right_eyebrow_len_ratio : float 
  nose_ratio : float
  face_area_ratio : float

cut1 = picture_weight(left_eye_len_ratio = 2.8181818181818183,
                      left_eye_area_ratio = 2.9473684210526314,
                      left_eyebrow_len_ratio = 1.0416666666666667,
                      right_eye_len_ratio = 2.25,
                      right_eye_area_ratio = 2.4516129032258065,
                      right_eyebrow_len_ratio = 1.0851063829787233,
                      nose_ratio = 1.1041666666666667,
                      face_area_ratio = 7.663756983240224
                      )

cut2 = picture_weight(left_eye_len_ratio = 2.2857142857142856,
                      left_eye_area_ratio = 2.1578947368421053,
                      left_eyebrow_len_ratio = 1.0294117647058822,
                      right_eye_len_ratio = 2.8333333333333335,
                      right_eye_area_ratio = 0.7142857142857143,
                      right_eyebrow_len_ratio = 1.0789473684210527,
                      nose_ratio = 1.1818181818181819,
                      face_area_ratio =0
                      )

cut3 = picture_weight(left_eye_len_ratio = 2.076923076923077,
                      left_eye_area_ratio = 2.3333333333333335,
                      left_eyebrow_len_ratio = 1.0930232558139534,
                      right_eye_len_ratio = 2.25,
                      right_eye_area_ratio = 1.7407407407407407,
                      right_eyebrow_len_ratio = 1.0888888888888888,
                      nose_ratio =  1.0714285714285714,
                      face_area_ratio =9.238388625592417
                      )

cut4 = picture_weight(left_eye_len_ratio = 2.8181818181818183,
                      left_eye_area_ratio = 2.9473684210526314,
                      left_eyebrow_len_ratio = 1.037037037037037,
                      right_eye_len_ratio = 2.8333333333333335,
                      right_eye_area_ratio = 0.7142857142857143,
                      right_eyebrow_len_ratio = 1.0357142857142858,
                      nose_ratio = 1.0416666666666667,
                      face_area_ratio =9.90168970814132
                      )

cut5 = picture_weight(left_eye_len_ratio = 2.526315789473684,
                      left_eye_area_ratio = 1.9875776397515528,
                      left_eyebrow_len_ratio = 1.0533333333333332,
                      right_eye_len_ratio = 2.3,
                      right_eye_area_ratio = 1.87292817679558,
                      right_eyebrow_len_ratio = 1.072289156626506,
                      nose_ratio = 1.0405405405405406,
                      face_area_ratio = 9.626238791882963
                      )
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
count = 0
a_w = 0
l_w = 0

drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
# For webcam input:
drawing_spec = mp_drawing.DrawingSpec(thickness=1, circle_radius=1)
cap = cv2.VideoCapture(0)
with mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as face_mesh:
  while cap.isOpened():
    success, image = cap.read()
    image_rows, image_cols, _ = image.shape
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(image)

    # Draw the face mesh annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_face_landmarks:
      for face_landmarks in results.multi_face_landmarks:
        landmark_dict = {}
        for idx, landmark in enumerate(face_landmarks.landmark):
          landmark_dict[idx] = face_draw.normalized_to_pixel_coordinates(landmark.x, landmark.y ,  image_cols, image_rows)
        # for idx in face_connections.LEFTIRIS:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
        # for idx in face_connections.RIGHTIRIS:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
        # for idx in face_connections.LEFTEYE:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
        # for idx in face_connections.RIGHTEYE:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA) 
        # for idx in face_connections.LEFTEYEBROW:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
        # for idx in face_connections.RIGHTEYEBROW:
        #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)
        # # for idx in face_connections.NOSE:
        # #   cv2.putText(image,str(idx), landmark_dict[idx],cv2.FONT_HERSHEY_PLAIN, 1, BLUECOLOR, 1, cv2.LINE_AA)    
        left_eye_area = face_draw.sum_area(landmark_dict, face_connections.LEFTEYEAREA)
        left_iris_length = face_draw.sum_line(landmark_dict, [(476,474)])
        left_eye_length = face_draw.sum_line(landmark_dict, [(362,363)])
        left_iris_area = face_draw.sum_area(landmark_dict,face_connections.LEFTIRISAREA)
        left_length_ratio = (left_eye_length/left_iris_length)
        left_area_ratio = (left_eye_area/left_iris_area)

        right_eye_area = face_draw.sum_area(landmark_dict, face_connections.RIGHTEYEAREA)
        right_iris_length = face_draw.sum_line(landmark_dict, [(471,469)])
        right_eye_length = face_draw.sum_line(landmark_dict, [(33,133)])
        right_iris_area = face_draw.sum_area(landmark_dict,face_connections.RIGHTIRISAREA)
        right_length_ratio = (right_eye_length/right_iris_length)
        right_area_ratio = (right_eye_area/right_iris_area)
        
        left_eyelength_weight = (cut3.left_eye_len_ratio-left_length_ratio)**2
        left_eyearea_weight = (cut3.left_eye_area_ratio-left_area_ratio)**2

        right_eyelength_weight = (cut3.right_eye_len_ratio-right_length_ratio)**2
        right_eyearea_weight = (cut3.right_eye_area_ratio-right_area_ratio)**2
        # print("left_area : {0}, left_length : {1}".format(left_eyearea_weight,left_eyelength_weight))
        # print("right_area : {0}, right_length : {1}".format(right_eyearea_weight,right_eyelength_weight))

        nose_bridge_length = face_draw.sum_line(landmark_dict, face_connections.NOSEBRIDGELINE)
        nose_horizon_length = face_draw.sum_line(landmark_dict, face_connections.NOSEHORIZONLINE)

        nose_length_ratio = (nose_bridge_length/nose_horizon_length)

        # nose_length_weight = (cut3.nose_ratio-nose_length_ratio)**2
        # # print('nose_length : {0}'.format(nose_length_weight))

        # left_eyebrowup_length = face_draw.sum_line(landmark_dict, face_connections.LEFTEYEBROWUP)
        # left_eyebrowdown_length = face_draw.sum_line(landmark_dict, face_connections.LEFTEYEBROWDOWN)

        # right_eyebrowup_length = face_draw.sum_line(landmark_dict, face_connections.RIGHTEYEBROWUP)
        # right_eyebrowdown_length = face_draw.sum_line(landmark_dict, face_connections.RIGHTEYEBROWDOWN)

        # left_eyebrow_ratio = (left_eyebrowup_length/left_eyebrowdown_length)
        # right_eyebrow_ratio = (right_eyebrowup_length/right_eyebrowdown_length)

        # left_eyebrow_weight = (cut3.left_eyebrow_len_ratio-left_eyebrow_ratio)**2
        # right_eyebrow_weight = (cut3.right_eyebrow_len_ratio -right_eyebrow_ratio)**2
        # # print('left : {0}, right : {1}'.format(left_eyearea_weight, right_eyearea_weight))
        # area_weight = left_eyearea_weight+right_eye_area
        # len_weight = left_eyebrow_weight+right_eyebrow_weight+nose_length_weight+left_eyelength_weight+right_eyelength_weight
        # a_w = a_w +area_weight
        # l_w = l_w +len_weight
        # count += 1
        # if count == 100:
        #   print('len : {0}, area : {1}'.format(l_w/100, a_w/100))
        #   count = 0
        #   a_w = 0
        #   l_w = 0
        face_area = face_draw.sum_area(landmark_dict, face_triangle_connection.triangle_conection)
        for n in face_connections.TWOEYEDISTANCE:
          x, y = landmark_dict[n]
          cv2.circle(image, (x, y), radius=2, color=(255,0,0), thickness=2)
        face_area_ratio = face_area/(left_eye_area+right_eye_area+(nose_bridge_length*nose_horizon_length))
        face_area_weight = ((cut4.face_area_ratio-face_area_ratio)**2)
        x, y = landmark_dict[382]
        cv2.circle(image, (x, y), radius=2, color=(255,0,0), thickness=2)
        # x, y = landmark_dict[0]
        # cv2.circle(image, (x, y), radius=2, color=(255,0,0), thickness=2)
        print(landmark_dict[0])
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Face Mesh', cv2.flip(image,1))       
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()