#Author: Foster C. Williams 
# 
#This is a very basic dndtools python script, it will have assorted things
#  such as dice rolls and other generation tools. 
#
#
#
#
import random;
def dice_roll():
	return random.randint(1,6);
def dice_roll(sides):
	return random.randint(1,sides);
