#To check a leap year or not

# here method declaration of isleapyear
def is_leap_year(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False
# Fetch input from user
year = int(input("ENTER YOUR YEAR HERE:"))
if is_leap_year(year):
  print("{} is a leap year.".format(year))
else:
  print("{} is not a leap year.".format(year))
