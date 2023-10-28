'''
Бот помічник, який розпізнає команди,
що вводяться з клавіатури,
та відповідає відповідно до введеної команди.
'''

def main():
    ''' main func'''
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
