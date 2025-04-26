def main():
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")


if __name__ == '__main__':
    main()