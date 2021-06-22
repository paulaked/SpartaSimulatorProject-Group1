from random import randrange


waiting_list = []
centre_list = ["The Theo Gluckstein Centre for Excellence", "Sam's Magic Academy (For Kids)",
               "Fahima's clan", "The Matt Brack-ademy ", "The Oscar School of 100%", "The 3rd wing of Andrew II's Estate",
               "Amy's Opera House", 'London', 'Beijing', 'The Moon', 'Sydney', 'Texas', 'Mexico City', 'Boscombe', 'Nice', 'Aberdeen',
               'Portland', 'Vernon', 'Kelowna', 'Amsterdam', 'Paris', 'Boston', 'Moscow', 'Frankfurt', 'Area 51',
               'Europa', 'The Void', "The Theo Gluckstein Centre for Disappointment", "Sam's Magic Academy (For Adults)",
               "Fahima's second and less important clan", "The Matthew Brack-ademy of Dance", 'The Oscar School of 200%',
               "The 4th wing of Andrew's country Manor", "Amy's Institute of Music and Natural History"]

open_centre_list = []
full_centres = []


def rand_centre_trainees():
    return randrange(0, 31, 1)

def create_centre():
    open_centre_list.append({'Name': centre_list[0], 'Active Trainees':[]})
    print(f"{centre_list[0]} created.")
    centre_list.remove(centre_list[0])


def all_centre_add():
    for cen in open_centre_list:
        add_trainee_to_centre(cen)

def add_trainee_to_centre(cen):
    random_number = rand_centre_trainees()
    print('Random number of trainees to go to centre:', random_number)
    for trainee in waiting_list[0:random_number]:
        if len(cen['Active Trainees']) < 100:
            cen['Active Trainees'].append(waiting_list[0])
            waiting_list.remove(waiting_list[0])

    print('Updated waiting list:', len(waiting_list))
    if len(cen['Active Trainees']) >= 100:
        print(f"{cen['Name']} is now full. No more trainees to be added.")
        if cen['Name'] not in full_centres:
            full_centres.append(cen['Name'])
    else:
        print(f"{cen['Name']} active trainees: {len(cen['Active Trainees'])}")

