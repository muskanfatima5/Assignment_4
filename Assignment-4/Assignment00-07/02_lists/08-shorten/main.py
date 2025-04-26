MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main():
    n = int(input("How many elements in the list? "))
    
    user_list = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        user_list.append(element)

    print("Original list:", user_list)

    shorten(user_list)

    print("Shortened list:", user_list)

if __name__ == '__main__':
    main()
