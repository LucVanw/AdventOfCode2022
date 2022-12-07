#!/usr/bin/env python3
from pathlib import Path
from collections import namedtuple

Command = namedtuple('Command', 'instruction inst_input output')
File = namedtuple('File', 'name size')

def parse_command(command):
    instr = command[1:3]
    instr_input, *instr_output = command[3:].split('\n')
    instr_output = list(filter(lambda x: x, instr_output))
    return Command(instruction = instr, inst_input=instr_input[1:], output=instr_output)

def parse_ls(output, current_location, locations):
    """
    location is modified inplace here! 
    """
    for out in output:
        first, second = out.split(' ')
        if first == 'dir':
            new_dir = current_location / second
            locations[new_dir] = []
            locations[current_location].append(new_dir)
        else:
            locations[current_location].append(File(name=second, size=int(first)))


def build_tree(commands):
    current_location = Path('/')
    locations = {current_location: []}
    for i, c in enumerate(commands[1:]):
        if c.instruction == 'ls':
            parse_ls(output=c.output, 
                     current_location=current_location, 
                     locations=locations)
             
        elif c.instruction == 'cd' and c.inst_input == '..':
            current_location = current_location.parent
            
        elif c.instruction == 'cd':
            current_location = current_location / c.inst_input
    return locations

def get_dir_size(key, all_locations):
    size, items = 0, all_locations[key]
    for item in items:
        if isinstance(item, File):
            size += item.size
        if isinstance(item, Path):
            size += get_dir_size(item, all_locations)  
    return size

with open("input.txt") as f:
    list_commands = list(map(parse_command, f.read().split('$')[1:]))
    
all_locations = build_tree(list_commands)
sizes = [get_dir_size(key, all_locations) for key in all_locations.keys()]

res1 = sum(filter(lambda x: x < 100000, sizes))
res2 = min(filter(lambda x: x + 70000000 - get_dir_size(Path('/'), all_locations) > 30000000, sizes))
print(f'Res 1: {res1}, Res 2: {res2}')
