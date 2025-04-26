def main():
    
  INCHES_PER_FOOT : int = 12

  feets = float(input("Enter the number of feets: "))
  inches : float = feets * INCHES_PER_FOOT
  print(f"There are {inches} inches in {feets} feets")


if __name__ == '__main__':
    main()