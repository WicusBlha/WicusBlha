#while loops = a statement that will execute its block of code
#              as long as its conditions remains true
#if you can't get out of a while loop, then its called an infinate loop
#e.g of a while loop:
#while 1==1: 
#   print("Help! i am stuck in a loop")
#create a name
name = ""
#if the length of the name is 0 then the loop continues, if not then the while loop stops
while len(name) == 0:
    name = input("Enter your username: ")
print("Hello "+name) 
#A shortcut of doing this is by doing
#name = None
#while not name:
#    name = input("Enter your usrname:")
#print("Hello "+name)#
