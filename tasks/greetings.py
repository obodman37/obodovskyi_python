# tasks/greetings.py
def process_input(user_input):
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if number > 7:
        say_hello()
    elif number == 7:
        print("Number is equal to 7.")
    else:
        print("Number is less than 7.")

def say_hello():
    print("Привет")
