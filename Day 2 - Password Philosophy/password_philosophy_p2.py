import numpy as np

f = open('D:\Projects\GitHub\Advent of Code 2020\Day 2 - Password Philosophy\inputs.txt', 'r')
inputs = []
nom = []
letter = []
pw = []
valid_pw = []

for line in f.readlines():
    inputs.append(line.split())

def sort_into_arr():
    for i in range(len(inputs)):
        nom.append(inputs[i][0].split("-"))
        letter.append(inputs[i][1].split(":"))
        pw.append(inputs[i][2])

sort_into_arr()
for i in range(len(letter)):
    letter[i].remove('')


def is_valid():
    for i in range(len(nom)):
        if(pw[i].count(letter[i][0]) >= int(nom[i][0]) and pw[i].count(letter[i][0]) <= int(nom[i][1])):
            valid_pw.append(pw[i])
    #if()
    return False

is_valid()

print(len(valid_pw))
