def process_name_input(user_input):
    if not user_input:
        print("Name is not provided.")
        return

    if user_input.isalpha() and user_input.lower() == "вячеслав":
        say_hello()
    else:
        print("Нет такого имени.")

def say_hello():
    print("Привет, Вячеслав")