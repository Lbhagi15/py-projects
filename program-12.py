# Write a program to convert the given seconds into hours – minutes – seconds

# entering the seconds through keybord
seconds=int(input("enter the seconds value"))

# converting the seconds  in minutes
minutes = (seconds/60)

#converting the seconds in hours
hours = (minutes/60)

#printinf the hours & minutes
print(f"minutes of {3600},{60} is {minutes}")
print(f"hours of {minutes},{60} is {hours}")
print("The End")