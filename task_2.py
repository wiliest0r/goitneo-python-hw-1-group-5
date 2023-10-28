'''
Бот помічник, який розпізнає команди,
що вводяться з клавіатури,
та відповідає відповідно до введеної команди.
'''

def parse_input(user_input):
    ''' parse input'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    ''' core func'''
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
