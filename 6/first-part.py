#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()

def are_different(s):
  return len(set(s)) == len(s)

indexes = []

row = rows[0]
print(f"Row : {row}")
for index in range(len(row)-3):
    string_to_compare = row[index:index+4]
    print(f"String : {string_to_compare}")
    if are_different(string_to_compare):
        print(f"Index : {index}")
        indexes.append(index)

print(f"Result = {indexes[0]+4}")
