#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()

elves = []
calories = 0

for row in rows:
    if row != "\n":
        calories += int(row)
    else:
        elves.append(calories)
        print(f"Elve {len(elves)} carries {calories} calories")
        calories = 0

elves.sort(reverse=True)

print(f"The solution is {elves[0]}")
