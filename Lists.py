# list = used to store multiple items in a single variabel
#create a variabel
meh = ["Youtube", "fmovies", "Eating", "Games", "Chess"]
#meh[0] = "Sleep"
#print(meh)
meh.append("Slap piggies")
meh.remove("Youtube")
meh.pop()
meh.insert(0,"Clean Dishes")
meh.sort()
meh.clear()
#Each item is the "list" is called a element in the meh variabel Youtube, Fmovies, Eating, Games, and Chess are all elements
#If you want to print a seccific elemt, use the indexes, e.g Youtube is 0, eating is 1 etc
#You can also update element 0 with something else

#i don't lilke the output ["Youtube", "fmovies", "Eating", "Games", "Chess"], so lets change that with a for loop we can print the thing without the square brackets
for x in meh:
    print(x)
#Fixed
#There are a few cool functions you can like append, string 6 has the append command
#You can also remove something if you'd like using the .remove command
#The .pop will remove the last element
#insert will make a new index at where ever you want it it to be
#last you got meh.sort, it will sort the elements, and the meh.clear this will clear all the elements of the meh