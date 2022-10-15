import string


colors = ["red", "white", "blue"]
colors.insert(2, "yellow")

print(colors)

animal = "Hippopotamus"

print(animal[3:6])
print(animal[-5])
print(animal[10:])


def squares(start, end):
	squares = []
	for x in range(start,end + 1):
		squares.append(x * x)
	return(squares)
	
print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def format_address(address_string):
  # Declare variables
 streetNumber = 0
 street = ""
  # Separate the address string into parts
 streetParts = address_string.split()
  # Traverse through the address parts
 for part in streetParts:
    # Determine if the address part is the
    # house number or part of the street name
  if part.isnumeric():
    streetNumber = part
  # Does anything else need to be done 
  # before returning the result?
  else:
    street += part + " "  
  # Return the formatted string  
 return "house number {} on street named {}".format(streetNumber,street)

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


b = " " 
d = ""
x = "Hello 50 am basic"
y = x.split()
print(y)
for element in y:
	#print(element)
	if element.isnumeric():
		d = element
	else:
	    b += element + " "

print("I have {} in {}".format(d,b))

def format_address(address_string):
  address_parts = address_string.split(" ")
  return "house number {} on street named {}".format(address_parts[0]," ".join(address_parts[1:])) 

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  #combined = list2 + list1.reverse() 
  list1.reverse()
  list2.extend(list1)
  return list2
	
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

def car_listing(car_prices):
  result = ""
  for car,price in car_prices.items():
    result += "{} costs {} dollars".format(car,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text.lower():
    # Check if the letter needs to be counted or not
    if letter.isalpha():
      if letter not in result:
        result[letter]= 1
    # Add or increment the value in the dictionary
      else:
        result[letter] += 1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}