def main():
    count_dict = {}  

    while True:
        num = input("Enter a number or press enter to stop: ")
        if num == "":
            break  
        try:
            num = int(num)  
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1
        except ValueError:
            print("Please enter a valid number.")

    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")

if __name__ == '__main__':
    main()