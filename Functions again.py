#functions (again) = a block of code that is executed when its called
#create a define function
def hello(first_name,last_name,age):
    print("Hello " +first_name+ " "+last_name) #You just made a function called hello, you also print "Hello!" Functions always end with a fair of parentheses
    print("You are "+str(age)+" years old")
    print("Ta da, functions complete!")
    
hello('Wicus','Nysschen',15)
#typing this in means that you called the hello() function, ez #You can call this function as many times as you'd like just type hello() again and again
#The "Bro" in the function is called a argument. They are info that you'r sending to a function
#You need a matching set of parameters you can call it what ever you want, I called it bro 