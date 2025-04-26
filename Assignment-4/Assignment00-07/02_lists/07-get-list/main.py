def main():
    user_list = []

    while True:
        value = input("Enter a value or press enter to stop : ")
        if value == "":
            break
        user_list.append(value)

    print("Here's the list:", user_list)

if __name__ == '__main__':
    main()
