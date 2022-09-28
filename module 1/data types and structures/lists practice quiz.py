def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    new = " " + word[1:] + word[:1] + "ay"
    say += "".join(new)
    # Turn the list back into a phrase
  say = say.strip()
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

#def guest_list(guests):
#	for guest in (guests):
#		print(guest)
#		# print(___.format(___))

#guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

##Click Run to submit code
#"""
#Output should match:
#Ken is 30 years old and works as Chef
#Pat is 35 years old and works as Lawyer
#Amanda is 25 years old and works as Engineer
#"""