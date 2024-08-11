def parse_input(user_input):
    """Розбирає введений користувачем рядок на команду та її аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """Додає новий контакт до словника контактів."""
    if len(args) != 2:
        return "Invalid command format. Please use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    if len(args) != 2:
        return "Invalid command format. Please use: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    """Виводить номер телефону зазначеного контакту."""
    if len(args) != 1:
        return "Invalid command format. Please use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

def show_all(contacts):
    """Виводить всі збережені контакти."""
    if not contacts:
        return "No contacts saved yet."
    else:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    """Основний цикл обробки команд."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
