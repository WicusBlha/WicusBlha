#set = collection which is unordered and unindexed. No duped values
#In order to make a set, you need to surround all values in curly braces, time to make a set
cat_stuff = {"Cat tv", "Cat nip", "Cat food", "Cat water filter", "Cat sandbox", "Metal music"} 
dog_stuff = {"Dog brush", "Dog treats", "Metal music"}

#Methods!
cat_stuff.add("Cat brush") 
#No print() stuff, its a set not a list
cat_stuff.remove("Cat sandbox")
#cat_stuff.clear()
cat_stuff.update(dog_stuff) #merge all the cat_stuff with dog_stuff
#Join two sets together and create a new set, make a new set:
farm_life = cat_stuff.union(dog_stuff)
#Too lazy to comare and contrast in english, mee too!
print(cat_stuff.intersection(dog_stuff)) #Compare
print(cat_stuff.difference(dog_stuff)) #Contrast

#Lets print it!
#for c in cat_stuff:
    #print(c)
    
#Doesnt add dupe values mean, if you add two "Cat nip" then it will only display that values once
