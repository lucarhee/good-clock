#! /usr/bin/env python3

Zero = ["#######", "#     #", "#     #", "#     #", "#     #", "#     #", "#######"]
One = ["##", "##", "##", "##", "##", "##", "##"]
Two = ["#######", "      #", "      #", "#######", "#      ", "#      ", "#######"]
Three = ["#######", "      #", "      #", "#######", "      #", "      #", "#######"]
Four = ["#     #", "#     #", "#     #", "#######", "      #", "      #", "      #"]
Five = ["#######", "#      ", "#      ", "#######", "      #", "      #", "#######"]
Six = ["#######", "#      ", "#      ", "#######", "#     #", "#     #", "#######"]
Seven = ["#######", "      #", "      #", "      #", "      #", "      #", "      #"]
Eight = ["#######", "#     #", "#     #", "#######", "#     #", "#     #", "#######"]
Nine = ["#######", "#     #", "#     #", "#######", "      #", "      #", "      #"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]


import time
import os
import sys


def print_big_digits(hours, minutes, seconds, SEPERATOR='   ', BIG_SEPERATOR='      '):
    output = ''
    lines = 0
    while lines < 7:
        if len(hours) > 1:
            output += Digits[int(hours[0])][lines] + SEPERATOR
            output += Digits[int(hours[1])][lines] + BIG_SEPERATOR
        else:
            output += Digits[0][lines] + SEPERATOR
            output += Digits[int(hours[0])][lines] + BIG_SEPERATOR

        if len(minutes) > 1:
            output += Digits[int(minutes[0])][lines] + SEPERATOR
            output += Digits[int(minutes[1])][lines] + BIG_SEPERATOR
        else:
            output += Digits[0][lines] + SEPERATOR
            output += Digits[int(minutes[0])][lines] + BIG_SEPERATOR

        if len(seconds) > 1:
            output += Digits[int(seconds[0])][lines] + SEPERATOR
            output += Digits[int(seconds[1])][lines] + '\n'
        else:
            output += Digits[0][lines] + SEPERATOR
            output += Digits[int(seconds[0])][lines] + '\n'

        lines += 1

    print(output)


def clock():
    while True:
        os.system('clear')
        now = time.strftime('%H:%M:%S')
        hours = now.split(':')[0]
        minutes = now.split(':')[1]
        seconds = now.split(':')[2]
        print_big_digits(hours, minutes, seconds)
        time.sleep(1)


def countdown(total_time):
    # total_time: minutes
    total_time = int(total_time) * 60  # in seconds
    while True:
        os.system('clear')
        left_time = total_time
        hours = str(left_time // 60 // 60)
        left_time = left_time - (int(hours) * 60 * 60)
        minutes = str(left_time // 60)
        left_time = left_time - (int(minutes) * 60)
        seconds = str(left_time)
        print_big_digits(hours, minutes, seconds)
        time.sleep(1)
        total_time -= 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1].isdigit:
        countdown(sys.argv[1])
    else:
        clock()
