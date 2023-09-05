#Loop control statements = change in loop execution from its normal sequence
#There are three of them
# break is used to terminate a loop
# continue skips tothe next iteration of the loop
# pass acts as a place holder


#Create a while loop
while True:
    name = input("Enter your name: ")
    if name  !="":
        break
    print(name)
    
#You can do this with a phone number too
phone_number = "123-456-7890"
for i in phone_number:
    if phone_number == "-":
        continue
    print(i, end="")
#This just prints your phone number without the dashes

for i in range (1,15):
    if i ==(12):
        pass
    else:
        print(i)
    