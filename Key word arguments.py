#keyword arguments = arguments that are preceeded by a identifier when we pass them to a function the order of the arguments doesnt matter, unlike positional arguments
#Python knowes the names of the arguments that our function recives
#Just like the previous lesson we use the function def, but we use the identifier
def favourite_cats(first,meh,nope):
    print("Wicus's favourite cats are: " +first+" "+meh+" "+nope)
    
favourite_cats(first='Lisa',nope='Bluey',meh='Ruby') #I made a function that calles wicus's favourite cats, there is another way you can order this. using the perameters first,meh,nope
#If you took the parameters out(first,meh,last) then it will be ordered in the way you ordered it. Its just more organized 