from centre_generator import *


#  Calling function returns a new random number. Need to assign to variable each month so maths
#  and print statements match
def rand_new_trainees():
    return randrange(20, 31, 1)  # generates number between 20-30, increment 1.


#  Creating a global variable for the student ID counter as this will need to retain the count outside of the function
#  it is used in.
stud_id_counter = 0


#  A function that adds new trainees to the waiting list based on a randomly generated number in a range.
def new_trainee_add():
    global waiting_list
    global stud_id_counter
    trainees = rand_new_trainees()  # Assigns random number of trainees to be created
    for i in range(1, trainees + 1):  # Adds each trainee to the waiting list
        waiting_list.append(stud_id_counter + i)  # Assigns trainees ID numbers
    stud_id_counter += trainees  # Adds number of trainees to ID so no duplicate ID values
    return stud_id_counter
