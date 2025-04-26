def main():
    print("First 20 even numbers:")
    for i in range(20):
        print(i * 2, end=' ') 
        # "end" means that the next print will be on the same line
    print()  

if __name__ == '__main__':
    main()