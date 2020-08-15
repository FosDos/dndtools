# Author: Foster C. Williams
# Github: Github.com/FosDos
#
# This script just generates some basic characteristics of an npc. 
# The dungeon masters manual was used to generate these tables of traits
#
import random;
import dndtools;

def main():
  npc_traits = gen_npc();
  for x in range(len(npc_traits)):
    print(npc_traits[x]);

def gen_npc():
  appearances = ["Distinctive jewelry","Piercings","Flamboyant or outlandish clothes","Formal, clean clothes","Ragged, dirty clothes", "Pronounced scar", "Missing teeth", "Missing fingers", "Unusual eye color", "Tattoos", "Birthmark", "Unusual skin color", "Bald", "Braided beard or hair", "Unusual Hair Color","Nervous eye twitch", "Distinctive Nose","Odd posture", "Exceptionally beautiful", "Exceptionally ugly"];
  talents = ["Plays a musical instrument", "Speaks serveral languages", "Unbelievably lucky", "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations", "Draws Beautifully", "Paints Beautifully", "Sings Beautifully", "Drinks everyone under the table", "Expert carpenter", "Expert cook", "Expert dart thrower", "Expert juggler", "skilled actor and master of disguise", "skilled dancer", "knows thieves cant"];
  mannerisms = ["Prone to singing, whistling, or humming quietly","Speaks in rhyme or some other peculiar way","Particularly low or high voice", "Slurs words, lisps, or stutters","Enunciates overly clearly", "Speaks loudly", "whispers", "Uses flowery speech or long words", "frequently uses the wrong words", "Uses colorful oaths and exclamations", "Makes constant jokes or puns", "Prone to predictions of doom", "Fidgets", "Squints", "Stares into the distance", "Chews things", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
  interaction_behaviors = ["Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot Tempered", "Irritable","Ponderous", "Quiet", "Suspicious"]
  bonds = ["dedicated to fulfilling a personal life goal", "Protective of close family members", "Protective of collegues or compatriots", "Loyal to a benefactor, patron, or employer", "Captivated by a romantic interest", "Drawn to some special place", "protective of a sentimental keepsake", "Protective of a valuable posession", "Out for revenge"]
  return [appearances[dndtools.dice_roll(20)-1], talents[dndtools.dice_roll(20)-1], mannerisms[dndtools.dice_roll(20)-1], interaction_behaviors[dndtools.dice_roll(12)-1], bonds[dndtools.dice_roll(8)-1]];

main();
