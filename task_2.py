'''
Бот помічник, який розпізнає команди,
що вводяться з клавіатури,
та відповідає відповідно до введеної команди.
'''

def parse_input(user_input):
    '''
    Processing of the entered text
    '''

    # split the entered string into separate words using a space as a separator
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    '''
    Create contact func.
    Returns the creation status.
    '''

    if len(args) != 2:
        return "Expected two arguments: name and phone number."
    input_name, phone = args # unpack args:
    if input_name in contacts:
        # print("user exists")
        return f'User with name {input_name} already exist.'
    contacts[input_name] = phone
    return "Contact added."

def change_contact(args, contacts):
    '''
    Update dictionary function.
    If success – returns contact status.
    '''

    if len(args) != 2:
        return "Expected two arguments."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        message = "Contact changed"
    else:
        message = "Contact does not exist."
    return message

def search_phone(args, contacts):
    '''
    Returns user phone number according to input username.
    '''

    input_name = args[0]
    if input_name in contacts:
        return contacts[input_name]
    return "User does not exist."

def main():
    '''
    Entry (main)
    '''

    # contacts = {}
    contacts = {'resu': '4321', 'user': '1234', 'fghj': '7654'}
    commands_list = ["hello",
                     "add [username] [phone]",
                     "change [username] [phone]",
                     "phone [username]",
                     "all","close or exit"]
    print("\nWelcome to the assistant bot!\n")
    print(f'Available commands: \n\n {" | ".join(commands_list)}\n')
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(search_phone(args, contacts))
        elif command == "all":
            for username, phone in contacts.items():
                print(f'Name: {username}, Phone: {phone}')
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
