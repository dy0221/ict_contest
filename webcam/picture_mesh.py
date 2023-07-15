

def pic_mesh() -> dict:
  #check webcam is available
  try:
    cap = cv2.VideoCapture(3)
  except:
    return
  #read image from webcam
  success, image = cap.read()
  
  if not success:
    cap.release()
    return
  
  #setup thresshold
  mp_face_mesh = mp.solutions.face_mesh.FaceMesh(max_num_faces=1,
                                                 refine_landmarks=True,
                                                 min_detection_confidence=0.5,
                                                 min_tracking_confidence=0.5)
  #identify image size
  image_rows, image_cols, _ = image.shape

  image.flags.writeable = False
  image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  #face mesh
  results = mp_face_mesh.process(image)

  image.flags.writeable = True
  image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
  #list to face ratio
  ratio_dict = {}
  landmark_dict = {}
  if not results.multi_face_landmarks:
    cap.release()
    return
  #calculate ratio use to landmark 
  for face_landmarks in results.multi_face_landmarks:
    for idx, landmark in enumerate(face_landmarks.landmark):

      landmark_dict[idx] = face_draw.normalized_to_pixel_coordinates(landmark.x, landmark.y ,  image_cols, image_rows)

      left_eye_area = face_draw.sum_area(landmark_dict, face_connections.LEFTEYEAREA)
      left_iris_area = face_draw.sum_area(landmark_dict,face_connections.LEFTIRISAREA)
      
      right_eye_area = face_draw.sum_area(landmark_dict, face_connections.RIGHTEYEAREA)
      right_iris_area = face_draw.sum_area(landmark_dict,face_connections.RIGHTIRISAREA)

      nose_bridge_length = face_draw.sum_line(landmark_dict, face_connections.NOSEBRIDGELINE)
      nose_horizon_length = face_draw.sum_line(landmark_dict, face_connections.NOSEHORIZONLINE)

      face_area = face_draw.sum_area(landmark_dict, face_triangle_connection.triangle_conection)
      face_length = face_draw.sum_line(landmark_dict, face_connections.FACELENGTHLINE)
      two_eye_distance = face_draw.sum_line(landmark_dict, face_connections.TWOEYEDISTANCELINE)
      face_area_ratio = face_area/(left_eye_area+right_eye_area+(nose_bridge_length*nose_horizon_length)\
                                   +left_iris_area+right_iris_area)
      face_length_ratio = face_length/two_eye_distance
      ratio_dict['face_length'] = face_length_ratio
      ratio_dict['face_area'] = face_area_ratio
      nose_lenght_ratio = nose_bridge_length/nose_horizon_length
      ratio_dict['nose_lenght'] = nose_lenght_ratio  

           
  cap.release()
  return ratio_dict
if __name__ =='__main__':
  import cv2
  import mediapipe as mp
  
  from webcam_package import face_draw
  from webcam_package import face_connections
  from webcam_package import face_triangle_connection
  while True:
    image = pic_mesh()
    print(image)
    
else :
  import cv2
  import mediapipe as mp
  
  from webcam.webcam_package import face_draw
  from webcam.webcam_package import face_connections
  from webcam.webcam_package import face_triangle_connection
        
