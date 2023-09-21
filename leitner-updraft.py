import csv
import random
import sys
import time

# Deck files are expected to be .csv files with the columns "front" and "back".
# All values in this table will be treated as strings.

def main():
	print("\nStudy start!\n")
	print("Drawing deck.")
	hand = getDeckFromCsv(sys.argv[1])
	repeatStash = []
	solvedStash = []

	allSolved = False
	while not allSolved:
		print("Shuffling hand.")
		random.shuffle(hand)

		for card in hand:
			print("\n--------------------------------\n")
			if (guessCard(card)):
				print("Placing card in solved stash.")
				solvedStash.append(card)
				time.sleep(0.5)
			else:
				print("Placing card in repeat stash.")
				repeatStash.append(card)
				time.sleep(0.5)
		
		if (len(repeatStash) == 0):
			allSolved = True
		else:
			print("Cards in hand depleted. Drawing cards from repeat stash.")
			time.sleep(2)
			hand = repeatStash
			repeatStash = []
	
	print("All cards solved! Goodbye.")

class Card:
	front: str
	back: str

def getDeckFromCsv(path: str) -> None:
	with open(path, "r", encoding = "utf-8") as csvContent:
		dictReader = csv.DictReader(csvContent)
		return list(dictReader)

def guessCard(card: Card) -> bool:
	print("Next card:\n")
	print(card["front"])
	input("\nPress Enter to reveal back side.\n")
	print(card["back"])
	solved = input("\nSolved correctly? (y/n) ")
	return solved == "y"

if __name__ == "__main__":
	main()