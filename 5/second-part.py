#!/usr/bin/env python3


file = open('input.txt', 'r')
rows = file.readlines()

def print_ship(ship):
    for stack in ship:
        for crate in stack:
            print (f"{crate}",end= "    ")
        print(f"\n")

def remove_blank(ship):
    for x in range(len(ship)):
        try:
            while True:
                ship[x].remove("")
        except ValueError:
            pass
    return ship

ship = []
n = 4

for row in rows[0:8]:
    line = []
    for index in range(0, len(row), n):
        line.append(row[index : index + n].strip().replace("[","").replace("]",""))
    ship.append(line)

ship = [list(x) for x in zip(*ship)]
ship = remove_blank(ship)

print_ship(ship)

orders = []
for row in rows[10:]:
    order = []
    row = row.split(" ")
    order.append(row[1])
    order.append(row[3])
    order.append(row[5].strip())
    orders.append(order)


for order in orders:
    start = int(order[1])-1
    end = int(order[2])-1
    counter = int(order[0])
    print (f"Order : ‘{order}")
    temp_crate = []
    while(counter):
        crate = ship[start].pop(0)
        temp_crate.insert(0,crate)
        counter -= 1
    counter = int(order[0])
    while(counter):
        crate = temp_crate.pop(0)
        ship[end].insert(0,crate)
        counter -= 1
    print_ship(ship)

print(f"RESULT : ",end="")
for stack in ship:
    print(f"{stack[0]}",end="")
