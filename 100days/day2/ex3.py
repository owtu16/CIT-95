# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# the max age of 90 minus my current age
max_age = 90 - int(age)

# variables save time left in months, weeks and days
max_age_in_months = max_age * 12
max_age_in_weeks = max_age * 52
max_age_in_days = max_age * 365

# print everything out using f-string
print(f"You have {max_age_in_days} days, {max_age_in_weeks} weeks, {max_age_in_months} months left")







