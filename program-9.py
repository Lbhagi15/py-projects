# Write a program to find your age in days.

# imports datetime package

from datetime import datetime

# need to  pass year , month,day

date_of_birth = datetime(1994, 10, 15)

#  subtract D.O.B with current date

count_days = datetime.today() - date_of_birth

#  printing age in days

print (f'Your Age in Days are {count_days.days}')
print("The end")