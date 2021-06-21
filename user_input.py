def months_input():
    entry = input("How many months would you like to run the simulator for? ")
    while True:
        try:
            value = int(entry)
            if value >= 0:
                break
            else:
                print("\nNumber cannot be negative. Please try again.")
                entry = input("How many months would you like to run the simulator for? ")

        except ValueError:
            print("\nMust be a number. Please try again.")
            entry = input("How many months would you like to run the simulator for? ")

    return value
