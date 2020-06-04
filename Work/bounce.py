# bounce.py
#
# Exercise 1.5
initial_drop_height = 100
rebound_factor = 3/5
number_of_bounces = 1

while (initial_drop_height * rebound_factor) > 0 and number_of_bounces<=10:
    initial_drop_height = initial_drop_height * rebound_factor
    print('bounce #:',number_of_bounces, 'Bounce Height:', round(initial_drop_height,4))
    number_of_bounces = number_of_bounces + 1