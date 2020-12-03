# (A)dvent (o)f (C)ode .py downloads the input for day of Advent of Code (https://adventofcode.com)
# The input will be downloaded into a file with the name <Day number>.txt. For example...
# Usage (for day 3):
# python aoc.py --day 3
# 
# Will download day 3 input file into a file on current working directory with name 3.txt
#
# Author: Jack Champagne
# Date: 12/3/2020
# 
# Prerequisite python modules:
# * requests
#
# pip install requests if you do not have it.
#
# Please use your cookie to make requests :) or else this will not work. See readme for instructions.


import requests
import sys

day = 1 # Nice and safe default

args = sys.argv
if len(args) >= 2:
    if '--day' in args:
        try:
            day_str = args[args.index('--day') + 1]
            day = int(day_str)
            if day not in range(1, 25):
                raise ValueError
        except ValueError as iden:
            print('--day ' + day_str + '\t is not a valid day. Aborting')
            quit()
    
    if '--auto' in args:
        print('Unimplemented')
        quit()

    if '--help' in args:
        print('''The input will be downloaded into a file with the name <Day number>.txt. For example...\n===Usage (for day 3)===\n  python aoc.py --day 3\n\nWill download day 3 input file into a file on current working directory with name 3.txt''')
        quit()
else:
    print('python aoc.py --help for help')

output = open(str(day) + '.txt', 'w')

session_cookie = open('my-cookie.txt' , 'r').readline() # PUT YOUR COOKIE HERE IF YOU LIKE LIKE SO OR PUT IN FIRST LINE OF FILE: 'session=641AE5.....'
my_headers = {'Cookie' : session_cookie}

puzzle_text = requests.get('https://adventofcode.com/2020/day/' + str(day) + '/input', headers=my_headers).text
output.write(puzzle_text)

output.close()