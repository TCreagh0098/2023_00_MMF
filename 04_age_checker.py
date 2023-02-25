# functions go here

# checks users enter an integer to a given question
def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Enter an integer innit fam")


# Main routine goes here
tickets_sold = 0

while True:

    name = input("Enter your name / xxx to quit: ")

    if name == "xxx":
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry pipsqueak you too young for this movie fool")
        continue
    else:
        print("?? Nad blud you ain't that old, please try again. ")
        continue

    tickets_sold += 1
