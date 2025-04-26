def main():

     temp = float(input("\033[1mEnter Tempertaure in Fahrenhiet: \033[0m"))
     degrees_celsius = (temp - 32) * 5.0/9.0
     
     print(f"Temperature : {temp}F = {degrees_celsius}C")

if __name__ == '__main__':
    main()