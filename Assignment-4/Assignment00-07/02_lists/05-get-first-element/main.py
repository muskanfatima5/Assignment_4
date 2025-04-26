def get_first_element(lst):
    print("First element:", lst[0])

def main():
    n = int(input("How many elements in the list? : "))

    user_list = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element)

    get_first_element(user_list)


if __name__ == '__main__':
    main()