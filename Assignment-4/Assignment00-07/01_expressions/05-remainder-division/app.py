def main():
    
    num1 = int(input("Enter the number for division : "))
    num2 = int(input("Enter the number for division : "))
    division : int = num1 / num2 
    remainder : int = num1 % num2

    print(f"The division of {num1} and {num2} is {division} with a remainder of {remainder}")


if __name__ == '__main__':
    main()