#for loop = a statement that willit block of code a limited time
# while loops = unlimited for loop = limited
#>>>for index in range(10):
#>>>    print(index+1)
#0-10 means 1-10 for computers, so what you can do is +1 in the print(index+1) or int the for index in range(10+1)
#wanna do 2 numbers??!
#>>>for outdex in range(50,100):
#>>>    print(outdex)
#The benefit of python is you can do strs too
#>>>for nextdex in "Time is up, countdown starting":
#>>>    print(nextdex)
#I don't know why you'd do that, but its a thing
#I made everything comments so that i can use the import time function. Erace the # before every >>> if you want to test this out too
import time
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Nudes leaked bitch")
#import time is the time function
#for senconds in range(10,0,-1): means a range starting at 10, ending at 0, time.sleep means 1 second cooldown after every number from 10 to 0 is passed, then it prints "Nudes leaked bitch"