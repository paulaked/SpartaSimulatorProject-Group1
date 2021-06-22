from centre_generator import *


#  Calling function returns a new random number. Need to assign to variable each month so maths
#  and print statements match
def rand_new_trainees():
    return randrange(20, 31, 1)  # generates number between 20-30, increment 1.


stud_id_counter = 0


def new_trainee_add():
    global waiting_list
    global stud_id_counter
    trainees = rand_new_trainees()  # assigns random number of trainees to be created
    for i in range(1, trainees + 1):  # adds each trainee to the waiting list
        waiting_list.append(stud_id_counter + i)  # assigns trainees ID numbers
    stud_id_counter += trainees  # adds number of trainees to ID so no duplicate ID values
