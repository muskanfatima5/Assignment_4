def main():
    
    num = float(input("\033[1mWrite any number:\033[0m"))
    square = num * num # or we can use num ** 2

    print(f"The square of {num} is {square}")

if __name__ == '__main__':
    main()