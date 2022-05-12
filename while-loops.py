def test_function():
    x = 0
    while x < 10:
     print("X is only " + str(x))
     x+=1
    print("X is now = " + str(x)) 

test_function()

def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  while n % 2 == 0:
    if n<=0:
      return False
    else:
      n = n / 2
      
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
    
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
print(is_power_of_two(80))