def main():
    
    days_in_year = 365
    hours_in_day = 24
    mins_in_hours = 60
    seconds_in_min = 60

    result : int = seconds_in_min * mins_in_hours * hours_in_day * days_in_year


    print(f"There are {result} seconds in a year")

if __name__ == '__main__':
    main()
