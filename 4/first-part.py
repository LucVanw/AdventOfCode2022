#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()


def fully_contains(first,second):
    first_group = set(range(int(first[0]),int(first[1])+1))
    second_group = set(range(int(second[0]),int(second[1])+1))
    print(f"First : {first_group}")
    print(f"Second : {second_group}")
    if first_group >= second_group:
        return True
    elif second_group >= first_group:
        return True
    else:
        return False


score_total = 0
for row in rows:
    sections = row.strip().split(",") 
    print(f"Sections : {sections}")
    if fully_contains(sections[0].split("-"),sections[1].split("-")):
        score_total += 1
        print(f"Fully Contained: {sections}")

print(f"Total : {score_total}")
