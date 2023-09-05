# nested loop = The "inner loop" will finish all iterations before finishing one iteration of the "outer loop"
rows = int(input("How many rows?: "))
colums = int(input("How many colums?:"))
#create the rows areiable folwed my the input function and the "How many rows?: " string, same with colums
symbol = input("Enter a symbol to use ")
#Lets create the outer loop
for i in range(rows):
    for j in range (colums):
        print (symbol, end = "")
        print()
        
#So a nested loop is just one loop inside another loop.