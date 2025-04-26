def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)  
    result = double(number)
    print(f"Double of {number} is {result}")

if __name__ == '__main__':
    main()