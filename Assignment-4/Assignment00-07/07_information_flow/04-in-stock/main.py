def num_in_stock(fruit):
    inventory = {
        'apple': 500,
        'banana': 300,
        'pear': 1000,
        'orange': 200
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
    
    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()