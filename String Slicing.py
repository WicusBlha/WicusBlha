#Time to slice some strings?
#Slicing = create a substring by exe elements from another string
#There are two methods for slicing. the indexing[] or the slice() function
#[start:stop:step]
#create a variable
name = "Lisa Baby"
#make substring
first_name = name[:4]
#Test this
print(first_name,)
#you need a stoping index aswell, both these fields are separated with a :, string 8 had been changed from [0] to [:3], python automatically think you use the o index if you leave it out
#remember the start index is inclusive and the stop index is exclucive this means if you say [0:3] the output will wlways say >>> Lis that is why you'd chance 3 with 4
#Create a last name
last_name = name[5:9]
print(last_name)
#Shortcut is you can just write [5:] because its the end of the str
#the step index counts every ___ name, want it to count every 2nd word, use the [5:9:2] at the end of the print statement to count, you guessed it, every 2nd name!
#First you need to create a new variable
funky_name = name[5:9:2]
#And print it!
print(funky_name)
reversed_name = name[::-1]
print(reversed_name)
#Now we use the slice() function
website = "http://google.com"
website_1 = "http://youtube.com"
#make a variable
slice = slice(7,-4)
#slice the https:// out, it is 7 indexes so say 7 and we are using the slice() function so instead of using : we use , so say 7, and -4 because why the hell not
#print it and your ready to go!
#You can reuse the slice() function asmany times as you want! All you need to add is the print
print(website[slice])
print(website_1[slice])
is_lisa_cute = input("Did you learn anything today: ")
is_lisa_cute_1 = input("Acctually idc")
print(is_lisa_cute_1)
source = "Source: https://youtu.be/XKHEtdqhLK8?t=3111"
time_laps = "Time laps: 51:51"
print(source)
print(time_laps)