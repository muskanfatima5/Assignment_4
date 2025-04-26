import math

def main():
    
   AB = float(input("What is the length of side AB : "))
   BC = float(input("What is the length of side BC : "))
   length_of_triangle : float = math.sqrt(AB ** 2 + BC ** 2)

   print("The length of CA(The hypotenuse) is : ",(length_of_triangle))

if __name__ == '__main__':
    main()