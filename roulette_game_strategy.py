# This is a demonstration of a gambling game strategy
# on the roulette
# The strategy is to play always the same color (red or black)
# until you win. Each time you lose you triple the bet and play same color
# Each time you win, you restart the bet to one dollar
# in theory you always win if you could triple your bet forever
# at some point it will always fall on your color
# problem is you run out of money due tu incremental bet being triple
# so, if you wander, what if I play this strategy un to a certain number?
# and play it for many times?
# will it add up to positive values or will I loose money?
# well, let's find out

import random

mon = 5000  # the money you start with
bw = 0  # the output ball (red or black)
ap = 1  # the starting bet (one dollar)
count = 0
play = 100  # the number of times you want to play
max = 7  # the number of times you can lose (1$,3$,9$,27$,81$,243$,729$,2187$...)

# you can play with numbers above
# play many times as you need, results very each time

# you can even play double instead of triple ***here***

for i in range(play):
    count = 0
    print(mon)
    while True:
        bw = random.randint(1, 2)
        count = count + 1
        if count < max:
            if bw == 2:
                mon = mon + ap
                ap = 1
                break
            else:
                ap = ap + ap * 2  # ***here***
        else:
            mon = mon - ap
            ap = 1
            break
