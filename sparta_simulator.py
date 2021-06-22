from user_input import *
from trainee_generator import *

months_max = months_input()
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
            create_centre()
        all_centre_add()
        print(f'There are currently {len(waiting_list)} trainees on the waiting list.')
        print(f'There are {number_of_centres} open centres.')
        print('Month over.\n')
        months_counter += 1
    endgame_outputs()

def endgame_outputs():
    print('\nEND OF SIMULATION \n-----------------')
    print('Total number of open centres:', len(open_centre_list))
    print('Number of open centres that are full:', len(full_centres))
    active_trainees = 0
    for cen in open_centre_list:
        active_trainees += len(cen['Active Trainees'])
    print('Number of trainees currently training:', active_trainees)
    print('Number of trainees on the waiting list:', len(waiting_list))