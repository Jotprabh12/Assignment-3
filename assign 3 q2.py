#question 2
print("Enter Date below to get date of next day.\n")

def leapyear(x):
# leap year condition
    if (x%400)==0 or ((x%100!=0) and (x%4==0)):
        return True
    else:
        return False

day=int(input("Enter Date [1-31]:"))
month=int(input("Enter Month [1-12]:"))
year=int(input("Enter Year [1800-2025]:"))
#condition 1
if day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    condition1=False
else:
    condition1=True

#List containing month with 31 days
month_31 = [1, 3, 5, 7, 9, 11]
#List containing month with 30 days
month_30 = [4, 6, 8, 10, 12]   
#for day entered 31 does not present in that month
c1a= day==31 and (month in month_30)
#for day entered greater than 29 in month february i.e 2
c1b= day>29  and month==2
#for day entered greater than 28 in february in non leapyear
c1c= day==29 and (not leapyear(year)) and month==2
if c1a or c1b or c1c :
    condition2=False
else:
    condition2=True

if c1a:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1b:
    print(f"\nError\n{day} day can't be in month {month}")
elif c1c:
    print(f"\nError\n{day} day can't be in month {month} as the year {year} in not leapyear")
elif condition1==False:
    print(f"\nError\nPlease enter date in range day[1-31], month[1-12], year[1800-2025] ")


if condition1==True and condition2==True :
#List containing month with 31 days
    month_31 = [1, 3, 5, 7, 9, 11]
#List containing month with 30 days
    month_30 = [4, 6, 8, 10, 12]
   
 #For month with 31 days
    if (month in month_31) == True:
        if day == 31:
            day = 1
            month = month + 1
        elif 1 <= day <= 30:
            day = day + 1

#For month with 30 days
    elif (month in month_30) == True:
        if day == 30 and month == 12:
            day = 1
            month = 1
            year = year + 1
        elif day == 30 and month != 12:
            day = 1
            month = month + 1
        elif 1 <= day <= 29:
            day = day + 1

    elif month == 2:
#For leap year
        if leapyear(year) == True:
            if day == 29:
                day = 1
                month = month + 1
            elif 1 <= day <= 28:
                day = day + 1

        elif leapyear(year) == False:
            if day == 28:
                day = 1
                month = month + 1
            elif 1 <= day <= 27:
                day = day + 1

    print(f"\nNext Date in format Day/Month/Year is: {day}/{month}/{year}")
