def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    user_input = int(input("Enter a number: "))
    print_divisors(user_input)

if __name__ == '__main__':
    main()