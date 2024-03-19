
year = int(input("Enter current year :"))

if year%4 == 0 :

    if year%100 == 0 :

        if year%400 == 0:

            print(f"{year} this year is leap year")

        else:
            print(f"{year} this year is not leap year3")
    else:
        print(f"{year} this year is leap year2")
else:
    print(f"{year} this year is not leap year1")