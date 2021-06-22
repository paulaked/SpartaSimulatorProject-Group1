from random import randrange
from user_input import *

#  Calling function returns a new random number. Need to assign to variable each month so maths
#  and print statements match
def rand_new_trainees():
    return randrange(20, 31, 1)  # generates number between 20-30, increment 1.

months_max = months_input()
waiting_list = []
stud_id_counter = 0

def new_trainee_add():
    global waiting_list
    global stud_id_counter
    trainees = rand_new_trainees()  # assigns random number of trainees to be created
    for i in range(1, trainees + 1):  # adds each trainee to the waiting list
        waiting_list.append(stud_id_counter + i)  # assigns trainees ID numbers
    stud_id_counter += trainees  # adds number of trainees to ID so no duplicate ID values
    print('New trainees:', trainees)
    print('Waiting list:', waiting_list)

def rand_centre_trainees():
    return randrange(10, 31, 1)

centre_list = ['Centre 1','Centre 2', 'Centre 3']

def add_centre(): # have a capacity variable that decreases depending on num of trainees in centre
    # can be done using lists. Use len(list) for calculations
#     centre = centre_list(months_counter/2)
    pass

def add_trainee_to_centre(): # will take in rand_centre_trainees and add that number of trainees from the waiting list, to the centre
    pass


def sparta_simulator():
    global months_max
    number_of_centres = 0
    months_counter = 0
    while months_counter <= months_max:
        print('Months passed:', months_counter)
        new_trainee_add()
        if months_counter %2 == 0 and months_counter > 0:
            number_of_centres += 1
            print('New centre added.')
            # add_centre()
        print(f'There are currently {len(waiting_list)} trainees.')
        print(f'There are {number_of_centres} open centres.')
        print('Month over.\n')
        months_counter += 1