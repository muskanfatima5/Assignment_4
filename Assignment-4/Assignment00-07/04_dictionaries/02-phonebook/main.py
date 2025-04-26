def main():
    phonebook = {}  

    while True:
        name = input("Enter a name (or press Enter to finish): ")
        if name == "":
            break  
        phone = input(f"Enter phone number for {name}: ")
        phonebook[name] = phone  

    print("\nPhonebook:")
    for name, phone in phonebook.items():
        print(f"{name}: {phone}")

if __name__ == '__main__':
    main()