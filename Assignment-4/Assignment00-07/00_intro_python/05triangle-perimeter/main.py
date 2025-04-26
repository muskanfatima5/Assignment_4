def main():
   
   side1 = input("\033[1mWhat is the length of side 1 :\033[0m")
   side2 = input("\033[1mWhat is the length of side 2 :\033[0m")
   side3 = input("\033[1mWhat is the length of side 3 :\033[0m")

   triangle_perimeter = float(side1) + float(side2) + float(side3)
   print(f"The total perimeter of a triangle is {triangle_perimeter}")

if __name__ == '__main__':
    main()