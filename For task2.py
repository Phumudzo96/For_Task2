# Ask user to enter the year they want to check if it is a leap year
year = int(input("What year do you want to start with: "))

# Ask user to enter the number of year they want to be checked
num_year = int(input("How many years do you want to check: "))

# Add the thee number of years  that are going to be checked to the number we starting at
num_year += 1
year1 = year + num_year

# Calculate which years are the leap years
for num in range(year, year1):
    if num % 4 ==0:
        print(f"{num} is a leap year")
    else:
        print(f"{num} is not a leap year")

