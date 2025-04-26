def main():
    fruit_prices = {
        "apple": 10.0,
        "durian": 25.0,
        "jackfruit": 20.0,
        "kiwi": 15.0,
        "rambutan": 9.5,
        "mango": 8.0
    }

    total_cost = 0.0

    for fruit, price in fruit_prices.items():
        try:
            quantity = int(input(f"\033[1mHow many {fruit} do you want :\033[0m"))
            total_cost += quantity * price
        except ValueError:
            print("Please enter a valid number.")

    print(f"\nYour total is ${total_cost}")

if __name__ == '__main__':
    main()