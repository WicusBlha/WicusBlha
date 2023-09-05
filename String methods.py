#String methods!!!
name = "Lisa Baby"
print(len(name))
#len= Lenght so print (len(name)) prints the lenght of the str name >>>5
print(name.find("L"))
#This command finds the character of the letter "L" in the name variable, in this case its index 0
#Wanna capitalize you name but your to lazy to press backspace and type in "w", no problem! type in an additional 24 characters by typing -->print(name.capitalize())
print(name.capitalize())
#To make the variable upper type: print(name.upper())
print(name.upper())
#same can be done with the print(name.lower()) command
print(name.lower())
print(name.isdigit())
#the .isdigit just outputs if the variable is a digit, duh,
print('Python is too easy')
print(name.isalpha())
#Are these alphabetical character? Don't know? .isalpha does!
#Can't count? Python does use the .count command!
print(name.count('a'))
#You need to replace your characters within your strings now! Why? Idc, use the .replace command, pass in two arguments like replace the 'a' with 'o' in "lisa" (Don't be a dumbass, arguments need to be in parenthasies)
print(name.replace("a", "o"))
#just for fun, you can use the "*" at the end of the print(name) to multiply the name variable by a given number like:
print(name*3)
print("Source: https://www.youtube.com/watch?v=XKHEtdqhLK8&")
print("Time stamp is 25:13 from 12:00:00")