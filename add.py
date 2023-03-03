def add(arg: dict) -> float or int:
  sum = 0
  key_list = [*arg]
  for num in key_list:
    sum += arg[num]
  return sum
def minus(time1: int, time2: int) -> bool:
  pass
if __name__ == '__main__':
#   num = add({'a':1, 'b':2})
#   print(num)
  import datetime
  current_time = datetime.datetime.now()
  with open('/home/dy/opencv_study_project/information.txt', "r") as f :
    name = f.read()
  name = name[:-2]
  information_list = []
  information_list = name.split(',')
  for information in information_list:
    information_info = information.split("  ")
    c_list = str(current_time).split(" ")
    c = c_list[1][:5]
    ca, cs = c.split(":")
    if ca[0] ==0:
      ca = ca[1]
    time = information_info[2]
    time_list = time.split(" ")
    t = time_list[1][:5]
    ta, ts = t.split(":")
    if ta[0]==0:
      ta = ta[1]
    ttm = int(ta)*60+int(ts)
    ccm = int(ca)*60+int(cs)

      
      
    print(ca)
    print(cs)