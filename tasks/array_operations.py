def process_array_input(user_input):
    try:
        array = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input. Please enter a valid list of numbers.")
        return

    print_multiples_of_three(array)

def print_multiples_of_three(array):
    result = [int(x) for x in array if x % 3 == 0]
    print("Elements divisible by 3:", result)