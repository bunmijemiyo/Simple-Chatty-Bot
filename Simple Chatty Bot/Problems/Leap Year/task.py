# put your python code here
leap_year = int(input())
if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")