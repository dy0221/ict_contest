import math
from typing import  Tuple, Union


def normalized_to_pixel_coordinates(
    normalized_x: float, normalized_y: float, image_width: int,
    image_height: int) -> Union[None, Tuple[int, int]]:
  """Converts normalized value pair to pixel coordinates."""

  # Checks if the float value is between 0 and 1.
  def is_valid_normalized_value(value: float) -> bool:
    return (value > 0 or math.isclose(0, value)) and (value < 1 or
                                                      math.isclose(1, value))

  if not (is_valid_normalized_value(normalized_x) and
          is_valid_normalized_value(normalized_y)):
    # TODO: Draw coordinates even if it's outside of the image bounds.
    return None
  x_px = min(math.floor(normalized_x * image_width), image_width - 1)
  y_px = min(math.floor(normalized_y * image_height), image_height - 1)
  return math.floor(x_px), math.floor(y_px)
    
def line_calculator(x1:int, y1:int, x2:int, y2:int ) -> int:
  x = (x1-x2)**2
  y = (y1-y2)**2
  return math.floor(math.sqrt(x+y))

def triangle_area(
    x1:int, y1:int, x2:int, y2:int, x3:int, y3:int) -> int :
  a = line_calculator(x1,y1,x2,y2)
  b = line_calculator(x1,y1,x3,y3)
  c = line_calculator(x2,y2,x3,y3)
  s = (a+b+c)/2
  area = (s*(s-a)*(s-b)*(s-c))**(1/2)  
  if type(area) is float:
    return math.floor(area)
  if type(area) is int:
    return area  

def sum_area(
  landmark:dict,
  connection: list):
  """
  landmark는 각 점의 위치를 나타냄 (x,y)
  connect는 어떤 점으로 삼각형을 만들지 나타냄(_,_,_)
  """
  area = 0
  for tuple in connection:
    try:
      f_point, s_point ,t_point = tuple
      f_pointx , f_pointy = landmark[f_point]
      s_pointx , s_pointy = landmark[s_point]
      t_pointx , t_pointy = landmark[t_point]
      s = triangle_area(f_pointx, f_pointy, s_pointx, s_pointy, t_pointx, t_pointy)
      area = area+s
    except:
      continue
  if area == 0:
    return 1
  return area

def sum_line(
  landmark:dict,
  connection: list):

  sum = 0
  for tuple in connection:
    f_point, s_point  = tuple
    try:
      f_pointx , f_pointy = landmark[f_point]
      s_pointx , s_pointy = landmark[s_point]
      length = line_calculator(f_pointx , f_pointy,s_pointx , s_pointy)
      sum = sum + length
    except:
      continue
  if sum ==0 :
    return 1
  return sum
                          
if __name__=='__main__':
  area =  0      
  

