#coding=utf8
import random
import time

def decision_num_chr():
  num_chr = {"num_lower":0,"num_upper":0,"num_figure":0}
  for i in range(9):
    tmp = random.randint(97,122)
    if tmp%3==0:
      num_chr["num_lower"]+=1

    elif tmp%3==1:
      num_chr["num_upper"]+=1

    elif tmp%3==2:
      num_chr["num_figure"]+=1

  return num_chr


#main
if __name__ == '__main__':
  while 1:
    num_chr = decision_num_chr()
    if num_chr["num_lower"]>1 and num_chr["num_upper"]>1 and num_chr["num_figure"]:
      break
  print num_chr

  for j in range(num_chr["num_lower"]):
    print chr(random.randint(97,122)),

  for j in range(num_chr["num_upper"]):
    print chr(random.randint(65,90)),
  
  for j in range(num_chr["num_figure"]):
    print chr(random.randint(48,57)),
