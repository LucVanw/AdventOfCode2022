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

score_total = 0
for group_number in range(int(len(rows)/3)):
    group = rows[group_number*3:group_number*3+3]
    print(f"group : {group}")

    common_list = set(group[0].strip()).intersection(group[1].strip()).intersection(group[2].strip())
    
    print(f"common : {common_list}")
    score_total += letter_value(common_list.pop())

print(f"Total : {score_total}")
