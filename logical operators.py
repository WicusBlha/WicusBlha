#logical operators (and, or, not)= used to check if two or more conditional statements are true
temp = int(input("Whats the temperature outside right now?: "))
if not (temp >= 25 and temp <= 35):
    print("Stop playing with python, and touch some grass")
elif not (temp < 25 and temp >35):
    print("Ok, ok, its not great, so go make some dough")
#or means as long as one of the if & and conditions are true then the entire staement is true
#not check one if statement instead of two or more if statements
#This can be done by closeing the statements in parenthisies
#if not (temp >=25 and temp <=35)
#do the save with the else if statements
#as you'd might expect, it does the opposite of what you asked it to do, like a little wicus