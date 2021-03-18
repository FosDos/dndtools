#Author: Foster C. Williams 
#
#This is a basic character rolling script, it uses the roll 4 drop 1 method for each stat
#
#Uses the dndtools library that has dice rolls and whatnot
#

#changing this to show peyton stuff

import random
import dndtools
def main():
	 stats = [0,0,0,0,0,0];
	 names = ["Strength: ","Dextrity: ","Constitution: ","Intelligence: ","Wisdom: ","Charisma: "];
	 for x in range(len(stats)):
	 	stats[x] = stat_roll();
	 for y in range(len(stats)):
	 	print(names[y] + str(stats[y]));

def stat_roll():
	values = [0,0,0,0];

	for x in range(len(values)):
		values[x] = dndtools.dice_roll(6);
	values = sorted(values);
	return sum_list(values[1:4]);

def sum_list(target):
	total = 0;
	for value in target:
		total = total + value;
	return total;
main();
