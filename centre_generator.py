#  Using randrange from random module to create the randomised elements of the code as they are all range-based.
from random import randrange


#  Creating an empty waiting list so that new trainees can be added.
waiting_list = []
#  Creating a centre list to draw names from
centre_list = ["The Theo Gluckstein Centre for Excellence", "Sam's Magic Academy (For Kids)", "Fahima's clan",
               "The Matt Brack-ademy ", "Oscar's Short-Back-And-Sides Hairdressing School",
               "The 3rd wing of Andrew II's Estate",
               "Amy's Opera House", 'London', 'Beijing', 'The Moon', 'Sydney', 'Texas', 'Mexico City', 'Boscombe',
               'Nice', 'Aberdeen', 'Portland', 'Vernon', 'Kelowna', 'Amsterdam', 'Paris', 'Boston', 'Moscow',
               'Frankfurt', 'Area 51', 'Europa', 'The Void', "The Theo Gluckstein Centre for Disappointment",
               "Sam's Magic Academy (For Adults)", "Fahima's second and less important clan",
               "The Matthew Brack-ademy of Dance", "The Oscar School of double 100%",
               "The 4th wing of Andrew's country Manor", "Amy's Institute of Music and Natural History"]

#  Creating a list for open centres to keep track of which centres the simulation can add trainees to.
open_centre_list = []
#  A full centres list as this is a required print statement at the end of simulation.
full_centres = []


#  The random number in a range generator for allocating a random number of trainees to each centre.
def rand_centre_trainees():
    return randrange(0, 31, 1)


#  A function to allocate a name from the centre list to newly created centres, removing them from the centre list so
#  that there are no repeating centre names.
def create_centre():
    open_centre_list.append({'Name': centre_list[0], 'Active Trainees': []})
    print(f"{centre_list[0]} created.")
    centre_list.remove(centre_list[0])


#  A separate function for adding trainees to a centre. This is called on in the following all_centre_add function.
#  print STATEMENTS FOR DEVS/DEMONSTRATION ONLY (not a requirement).
def add_trainee_to_centre(cen):
    random_number = rand_centre_trainees()
    print('Random number of trainees to go to centre:', random_number)
    for trainee in waiting_list[0:random_number]:
        if len(cen['Active Trainees']) < 100:
            cen['Active Trainees'].append(waiting_list[0])
            waiting_list.remove(waiting_list[0])
    print('Updated waiting list:', len(waiting_list))
    #  Only allocate trainees if there are less than 100 on the active trainees list.
    if len(cen['Active Trainees']) >= 100:
        print(f"{cen['Name']} is now full. No more trainees to be added.")
        if cen['Name'] not in full_centres:
            full_centres.append(cen['Name'])
    else:
        print(f"{cen['Name']} active trainees: {len(cen['Active Trainees'])}")


#  Function for assigning trainees to centres, looping through the open centres.
#  As mentioned above, the adding trainees function is separate to allow for future adaptions to how trainees are
#  allocated to a centre.
def all_centre_add():
    for cen in open_centre_list:
        add_trainee_to_centre(cen)
