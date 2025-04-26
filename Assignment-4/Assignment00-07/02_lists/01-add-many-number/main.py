def list_of_numbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    my_list = [10, 20, 30, 40]
    result = list_of_numbers(my_list)
    print("Sum:", result)  

if __name__ == '__main__':
    main()