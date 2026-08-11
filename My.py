print("Hello World")
earningsgoal = input("How much money do you need to save in a year? ")
months = int(earningsgoal) / 12
weeks = months / 4
days = weeks / 7
print("To save up " + earningsgoal + " dollars in one year, you will need to save $" + str(round(months, 2)) + " per month.")
print("To save up " + str(months) + " dollars in one month, you will need to save $" + str(weeks) + " per week.")
print("To save up " + str(weeks) + " dollars in one week, you will need to save $" + str(days) + " per day.")