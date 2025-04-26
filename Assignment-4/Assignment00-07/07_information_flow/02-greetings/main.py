def greet(name):
    print(f"Greetings {name}!")

def main():
    name = input("\033[1mWhat's your name : \033[0m")
    greet(name)

if __name__ == '__main__':
    main()
