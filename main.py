from tasks.greetings import process_input
from tasks.check_name import process_name_input
from tasks.array_operations import process_array_input

if __name__ == "__main__":
    print("1. Если введенное число больше 7, то вывести 'Привет':")
    user_input = input("Enter a number: ")

    try:
        process_input(user_input)
    except ValueError as e:
        print(f"Error: {e}")

    print("-" * 10)

    print("2. Если введенное имя совпадает с 'Вячеслав', то вывести 'Привет, Вячеслав', если нет, то вывести 'Нет такого имени':")
    user_input1 = input("Enter a name: ")

    try:
        process_name_input(user_input1)
    except ValueError as e:
        print(f"Error: {e}")

    print("-"*10)

    print("3. На входе есть числовой массив, необходимо вывести элементы массива кратные 3:")
    user_input2 = input("Enter a space-separated list of numbers: ")

    try:
        process_array_input(user_input2)
    except ValueError as e:
        print(f"Error: {e}")