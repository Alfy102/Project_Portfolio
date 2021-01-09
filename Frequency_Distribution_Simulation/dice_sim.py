#Usage: dice_sim.py "numbers of die" "numbers of die face" "number of roll"
from collections import Counter
import random
import sys

dice_no = int(sys.argv[1])
dice_face = int(sys.argv[2])
dice_roll = int(sys.argv[3])

roll_set=[]
for m in range(dice_roll):
    dice_set=[]
    #-----------------dice roll------------------------
    for n in range(dice_no):
        dice = random.randint(1,dice_face)
        dice_set.append(dice)
    #--------------------------------------------------
    roll_set.append(sum(dice_set))
#print(roll_set)
#Since there are n number of dice, the minimum sum of the total dice must be the value of dice_no. 
#The maximum sum of a dice roll is the number of dice_face multiply by dice_no


#---------------------count unique values in array-----------------
print(Counter(roll_set))

#for x in range(dice_no,(dice_no*dice_face)+1):
#    y=0
#    for z in range(len(roll_set)):
#       if x==roll_set[z]:
#            y+=1
#    print(x,y)