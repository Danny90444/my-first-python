

def mary_sue(fname):
    # ("There is no " + fname)
    return(fname)

mary_sue("spoon")    

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("cat" == "cat")


print( "this is " + str(1 / 4))

def fractional_part(numerator, denominator):
	if denominator == 0 or numerator == 0:
		return 0
	div = (numerator % denominator)
	if div > 0:
			rem = (div / denominator)
			return rem
	elif div == 0:
			 return 0
		
		

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

def format_name(first_name, last_name):
	if last_name and first_name:
		return ("Name: " + last_name + ", " + first_name)
	if len(first_name) > 0: 
		return("Name: " + first_name)
	elif len(last_name) > 0: 
		return("Name: " + last_name )
	elif not first_name and last_name:
		return ("")


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string