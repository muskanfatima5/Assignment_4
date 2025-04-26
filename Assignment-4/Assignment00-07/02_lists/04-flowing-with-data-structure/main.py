def add_three_copies(my_list, data):
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    messages = input("\033[1mEnter a message to copy :\033[0m")
    message = []

    print("List before:", message)

    add_three_copies(message, messages)

    print("List after:", message)

if __name__ == '__main__':
    main()