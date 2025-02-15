import random 
import csv
check=False
num=0

with open('try.csv', newline='') as csvfile:
    riddle = list(csv.reader(csvfile))
again=1
count = 0
while again== 1:
    num=random.randint(1,len(riddle))
    print(riddle[num][0])
    trial=input("What is your answer?")
    if riddle[num][5] in trial:
        check= True
        print("You are correct")
    while trial != riddle[num][5] and check == False and count<6:
      print("Try again")
      trial=input("What is your answer?")
      count = count+1
      if riddle[num][5] in trial:
        check= True
      if count==1 and check== False:
        print(riddle[num][1])
      elif count==3 and check== False:
        print(riddle[num][2])
      elif count==5 and check== False:
        print(riddle[num][3])
      elif count>5 and check== False:
        print(riddle[num][4])  
      if trial == riddle[num][5]:
        print("You are correct")
    retry=input("Would you like to play again?")
    if retry=="yes":
        again=1
    else:
       again=0
