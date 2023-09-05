#nested function calls = function calls inside the function calls, innermost function calls are resolved first, returned value is used as arguments for the next outer function
apple = input("Good afternoon, Apple here, please enter your age: ")
apple = float(apple)
apple = abs(apple)
apple = round(apple)
apple_1 = input("Did you mean "+str(apple) +" You can only use letters: y, and n: ")
if apple_1 == "y":
    print("Thank you!")
elif apple_1 == "n":
    print("Well, here at apple we don't really care, you are 14, deal with it. Also your age is now stored in out databse and will be sold to hacker for extra profit, Thank you for using apple :D")
age = apple_1
print("Your age is: "+str(apple))