#dictionary = A chaneable, unordered collection of unique key: value pairs. Its fast bc it uses hashing, allow us to access a value quickly
capitals = {'USA': 'Washington DC',
            'India': 'new Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'} #use curly braces bc its a dictionary, Usa is a key and washington dc is a value sperate the two with a colon and a comma followed with a space
  
#You can use the update method to add a key:value to the dictionary
capitals.update({'Germany': 'Berlin'})
#or you can change the value of a key
capitals.update({'USA': 'Alaska'})
#The .pop removes stuff wanna remove the usa's greatest threat?
capitals.pop('China') #no need for the curly braces, we are not adding/updating anything
capitals.clear()

#Dictionaries are different, we use the associated key with that value e.g
#print(capitals.['Russia']) #capitals then to access a element in the capitals of russia use the stright braces anf in '' (Doesnt work, just an e.g)
#This is not safe so the easier and more reliable way is to use the get method
print(capitals.get('South Africa')) #using south africa as a e.g, this will return none, when the [] method would encouter a error
print(capitals.keys()) #Will print the keys
print(capitals.values()) #Will print the values
print(capitals.items()) #EVERYTHING

#To print the entire dictionary use a for loop
for key,value in capitals.items():
    print(key, value)
