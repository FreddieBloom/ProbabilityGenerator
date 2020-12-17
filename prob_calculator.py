import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.__dict__.update(kwargs)
    contents=[]
    for key in self.__dict__:
      for x in range(self.__dict__.get(key)):
        contents.append(key)
    self.contents= contents
  
  def draw(self,num_balls_drawn):
    randomlist = []
    templist = self.contents[:]
    if num_balls_drawn <= len(templist):
      for x in range(num_balls_drawn):
        popped = templist.pop(random.randint(0, len(templist)-1))
        randomlist.append(popped)
      return randomlist 

    else:
      return self.contents
    #print(randomlist)
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matches = 0
  for x in range(num_experiments):
    timesfound = Counter(hat.draw(num_balls_drawn))
    result = ""
    for keys in expected_balls:
      if timesfound[keys] >= expected_balls[keys]:
        pass
      else:
        result = "wrong"
    if result != "wrong":
      matches+=1
  return matches/num_experiments
  


