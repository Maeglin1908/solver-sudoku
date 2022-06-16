import os
import sys
from termcolor import colored

filename = sys.argv[1]

grid = []
saved = []

def check():
	for lig in range(9):
		alreadyUsed = []
		for col in range(9):
			v = grid[lig][col]
			if v != 0 and v in alreadyUsed:
				return False

	alreadyUsed = []
	for col in range(9):
		alreadyUsed = []
		for lig in range(9):
			v = grid[lig][col]
			if v != 0 and v in alreadyUsed:
				return False

	alreadyUsed = []
	cell_lig = (lig // 3) * 3
	cell_col = (col // 3) * 3
	for i in range(3):
		for j in range(3):
			v = grid[cell_lig + i][cell_col + j]
			if v != 0 and v in alreadyUsed:
				return False

	return True

def getValidNumbers(lig, col):
	alreadyUsed = set([])
	for i in range(9):
		v = grid[lig][i]
		if v != 0:
			alreadyUsed.add(v)

		v = grid[i][col]
		if v != 0:
			alreadyUsed.add(v)
	cell_lig = (lig // 3) * 3
	cell_col = (col // 3) * 3
	for i in range(3):
		for j in range(3):
			v = grid[cell_lig + i][cell_col + j]
			if v != 0:
				alreadyUsed.add(v)
	valids = [a for a in range(1, 10) if a not in alreadyUsed]
	return valids


tries = 0
def solve(lig, col):	
	global tries
	tries += 1
	nextCol = col + 1
	nextLig = lig
	if nextCol == 9:
		nextCol = 0
		nextLig += 1

	# grid is solved
	if nextLig == 9:
		print("Solved in ", tries, "tries")
		display()
		return True

	if grid[nextLig][nextCol] > 0 and check() and solve(nextLig, nextCol):
		return True

	validNumbers = getValidNumbers(nextLig, nextCol)
	for vn in validNumbers:
		grid[nextLig][nextCol] = vn
		if check() and solve(nextLig, nextCol):
			return True
		grid[nextLig][nextCol] = 0

	return False


def display():
	line = "+---+---+---++---+---+---++---+---+---+"
	print("\n\n")
	for i, row in enumerate(grid):
		print(line)
		if i % 3 == 0 and i > 0:
			print(line)
		line_numbers = "|"
		for j, n in enumerate(row):
			if j % 3 == 0 and j > 0:
				line_numbers += "|"
			sn = " " + (str(n) if n > 0 else " ") + " "
			csn = sn if saved[i][j] != 0 else colored(sn, 'green', attrs=['reverse'])
			line_numbers += csn + "|"
		print(line_numbers)
	print(line)


with open(filename) as f:
    for row in f.readlines():
        grid.append( [int(x) for x in row.strip()] )
saved = [r.copy() for r in grid]

solve(0,-1)