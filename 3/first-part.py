#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()
score_total = 0

def letter_value(character):
    print(f"Commun : {character}")
    value = ord(character)
    if value >= 97:
        value -= 96
    elif value <= 90:
        value -= 38
    return value

for row in rows:
    half = int(len(row)/2)
    first_compartment = list(row[:half])
    second_compartment = list(row[half:])
    common_list = set(first_compartment).intersection(second_compartment)

    score = letter_value(common_list.pop())
    score_total += score

    print(f"value : {score}")
print(f"Total : {score_total}")
