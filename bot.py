def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        func_name=str(func).split(" ")[1]
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func_name == "add_contact":
                return "Please write command 'add => name => phone'"
            elif func_name == "change_number":
                return "Please write command 'change => name => new phone'"
        except KeyError:
            if func_name == "change_number":
                return "There is no contact with this name in your list,\
                    \n if you want to add it, please write command - 'add => username => phone'"
        except IndexError:
            if func_name == "phone_username":
                return "Please write command 'phone => name'"    
    
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    name = name.capitalize()
    if name not in contacts:
        if name.isalpha()== True and phone.isdigit() == True:
            contacts[name] = phone
            return f"Contact {name} - {phone} added."
        else:
            return "Please write command 'add' => 'name' in letters => 'phone' in numbers'"
    else:
        return f"There is already contact with this name,\
            \n if you want to change it, please write command - 'change => username => phone'"

  
@input_error
def change_number(args, contacts):
    name, phone = args
    name = name.capitalize()
    contacts.pop(name)
    if phone.isdigit() == True:
        contacts.update({name: phone})
        return f"Contact {name} changed to {phone}"
    else:
        return "Please write command 'change' => 'name' in letters => 'phone' in numbers'"
    
       
@input_error
def phone_username(args, contacts):
    name = args
    name = name[0].capitalize()
    if name in contacts:
        return f"Contact with name {name} - {contacts.get(name)}"
    else:
        return "There is no contact with this name in your list,\
                    \n if you want to add it, please write command - 'add => username => phone'" 


def show_all_conacts(contacts):
    contacts_list = ""
    for name, phone in contacts.items():
        contacts_list += name + " - " + phone + "\n"
    return f"{contacts_list}"

def main():
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
            print(change_number(args, contacts))
        elif command == "phone":
            print(phone_username(args, contacts))
        elif command == "all":
            print("Your contacts list:")
            print(show_all_conacts(contacts))
        else:
            print("Invalid command.") 
    return contacts       
               

if __name__ == "__main__":
    main()
    

