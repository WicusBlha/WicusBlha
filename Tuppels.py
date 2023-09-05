#tupel = collection which is ordered and unchangeable, used to group together related data
#Create a variable
wicus = ("Wicus", "15", "Male")
#There are three methonds for a tupel
print(wicus.index("Wicus")) #The index of the word Wicus (0)
print(wicus.count("Wicus")) #How many times "Wicus" pops up in the wicus wariable

#Display all the contence of a tuple using a for loop
for w in wicus:
    print(w)
    
#certian value exixts within our tuple useing if statements
if "Wicus" in wicus:
    print("Wussup, master programmer in da house!")

