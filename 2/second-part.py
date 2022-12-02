#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()

score_total = 0

def hand_point(hand):
        match hand:
            case 'A':
                return 1
            case 'B':
                return 2
            case 'C':
                return 3

def which_hand(hand,goal):
        match goal:
            case 'X':
                if hand == 'A':
                    return 'C'
                if hand == 'B':
                    return 'A'
                if hand == 'C':
                    return 'B'
            case 'Y':
                return hand
            case 'Z':
                if hand == 'A':
                    return 'B'
                if hand == 'B':
                    return 'C'
                if hand == 'C':
                    return 'A'

def match_point(goal):
        match goal:
            case 'X':
                return 0
            case 'Y':
                return 3
            case 'Z':
                return 6

for row in rows:
        shape = row.split()
        score = 0
        my_hand = which_hand(shape[0],shape[1])

        score += hand_point(my_hand)
        score += match_point(shape[1])

        print(f"I want to : {shape[1]} so {shape[0]} vs {my_hand} = {score}")
        score_total += score

print(f"Total = {score_total}")
