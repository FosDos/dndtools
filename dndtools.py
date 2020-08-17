#Author: Foster C. Williams 
# 
#This is a very basic dndtools python script, it will have assorted things
#  such as dice rolls and other generation tools. 
#
#
#
#
import random;
import math;
def dice_roll():
	return random.randint(1,6);
def dice_roll(sides):
	return random.randint(1,sides);
def stat_to_bonus(stat):
	return math.floor((stat-10)/2);
def bonus_test():
	for x in range(1,31):
		print(str(x) + ": " + str(stat_to_bonus(x)));
