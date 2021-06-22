from trainee_generator import rand_trainee

# centre_trainees = []
waiting_list = []
id = 0


def waiting_list_add():
    trainees = rand_trainee()  # assigns random number of trainees to be created
    print('New trainees ', trainees)
    for i in range(1, trainees + 1):  # adds each trainee to the waiting list
        waiting_list.append(id + i)  # assigns trainees ID numbers
    id += trainees  # adds number of trainees to ID so no duplicate ID values
    print(waiting_list)
    print('Id', id)


waiting_list_add()

# centre_add = 25
# for i in range(0, centre_add):
#     centre_trainees.append(i)
#     waiting_list.remove(i)
#
# print('Centre trainees new', centre_trainees)
# print('Waiting list new', waiting_list)
