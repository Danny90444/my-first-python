fruits = ['pineapple', 'banana', 'apple', 'orange']
print(fruits)
fruits.pop(3)
print(fruits)

fruits[2] = "strawberry"
print(fruits)

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
		# Iterate through the list
	for x in elements:
		# Does this element belong in the resulting list?
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(x)
		# Increment i
		i = i + 1
	
	return new_list
 

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

def skip_elements(elements):
	# Initialize variables
	new_list = []
	i = 0
		# Iterate through the list
	for x in range(0,len(elements),2):
		# Does this element belong in the resulting list?
		if len(elements) != 0:
			# Add this element to the resulting list
			new_list.append(elements[x])
		# Increment i
		i += i 
	
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']

animals = ["lion", "zebra", "dolphi n","monkey"]
chars = 0 
for animal in animals:
	chars += len(animal) 

print("Total characters: {}, Average legnth: {}".format(chars, chars/(len(animals))))

winners = ["Ashley", "Dylan", "Reese"]
for index,person in enumerate(winners):
	print(" {} - {}".format(index +1, person))