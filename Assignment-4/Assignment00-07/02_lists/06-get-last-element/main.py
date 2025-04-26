def get_last_element(lst):
    print("Last element:", lst[-1])

def main():
    n = int(input("How many elements in the list? : "))

    user_list = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element)

    get_last_element(user_list)

if __name__ == '__main__':
    main()
