#index operator [] = gives gives access to sequence's element [str, list, tupels]
name = "wicus nysschen!"
#if(name[0].islower()): #is the first letter of the str lowercase? if it is
#    name = name.capitalize() #make it caped.
    
first_name = name[:5].upper() #With the index operator you can specify the range. Starting at index 0 then ending at index 4. using the .upper method, you can make it uppercase
print(first_name)
#Create a sub string for last name
last_name = name[6:].upper()
print(last_name)
#Cool thing to remember, -1 in python means last, -2 means second-to-last and so on