#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()

elves = []
calories = 0

score_total = 0

def hand_point(hand):
        match hand:
            case 'X':
                return 1
            case 'Y':
                return 2
            case 'Z':
                return 3


def match_point(hand1,hand2):
    if hand1 == 'A':
        if hand2 == 'X':
            return 3
        if hand2 == 'Y':
            return 6
        if hand2 == 'Z':
            return 0
    if hand1 == 'B':
        if hand2 == 'X':
            return 0
        if hand2 == 'Y':
            return 3
        if hand2 == 'Z':
            return 6
    if hand1 == 'C':
        if hand2 == 'X':
            return 6
        if hand2 == 'Y':
            return 0
        if hand2 == 'Z':
            return 3



for row in rows:
        shape = row.split()
        score = 0
        score += hand_point(shape[1])
        score += match_point(shape[0],shape[1])

        print(f"{shape[0]} vs {shape[1]} = {score}")
        score_total += score

print(f"Total = {score_total}")
