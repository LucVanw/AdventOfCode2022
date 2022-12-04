#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()


def overlaps(first,second):
    first_group = set(range(int(first[0]),int(first[1])+1))
    second_group = set(range(int(second[0]),int(second[1])+1))
    if first_group & second_group :
        print(f"Intersection : {first_group.intersection(second_group)}")
        return True
    else:
        return False


score_total = 0
for row in rows:
    sections = row.strip().split(",")
    print(f"Sections : {sections}")
    if overlaps(sections[0].split("-"),sections[1].split("-")):
        score_total += 1
        print(f"Fully Contained: {sections}")

print(f"Total : {score_total}")
