# Plant irrigation schedule.
# (If the time is 6:00 am and the weather forecast says no rain, and it has not rained in last 12 hours.) - activate
# or
# ( soil is dry, and the weather forecast says no rain) - activate

# Asking user for input of true or false along with listing variables
time = (input("It is 6:00 am? (True or False):"))
weatherForecast = (input("The forecast said there is no rain? (True or False):"))
rainedInLastHours = (input("It has not rained in the last 12 hours? (True or False):"))
soilDry = (input("The soil is dry? (True or False):"))

# If statement, so scenario can be activated or deactivated based on what the user types in (True or False)
if (soilDry == "True" and weatherForecast == "True") or (time == "True" and weatherForecast == "True" and
                                                         rainedInLastHours == "True"):
    print("Water system is activated!")
else:
    print("Water system is deactivated! Already had water.")
