from operator import length_hint


fruits = ['pineapple', 'banana', 'apple', 'orange']
print(fruits)
fruits.pop(3)
print(fruits)

fruits[2] = "strawberry"
print(fruits)

def skip_elements(elements):
	#code goes here
	result = []
		# Iterate through the list
	for index, element in enumerate(elements):
		# Does this element belong in the resulting list?
		if index % 2 == 0:
			# Add this element to the resulting list
			result.append(element)
	return result
 

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

animals = ["lion", "zebra", "dolphin","monkey"]
chars = 0 
for animal in animals:
	chars += len(animal) 

print("Total characters: {}, Average legnth: {}".format(chars, chars/(len(animals))))

winners = ["Ashley", "Dylan", "Reese"]
for index,person in enumerate(winners):
	print(" {} - {}".format(index +1, person))


multiples = []
for x in range (1,11):
	multiples.append(x*7)

print(multiples)

# List comprehension
muliples = [x*7 for x in range(1,11)]
print(multiples)

langauges = ["Python", "Go", "Ruby", "Java", "C", "Perl"]
lengths = [len(langauge) for langauge in langauges]
print(lengths)
z = [x for x in range(0,101) if x %3 == 0]
print(z)

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2!= 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []