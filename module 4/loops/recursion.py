def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

def is_power_of(number, base):
    if number < base: 
        if number == 1: 
            return True
        else: return False
     
    return is_power_of((number/base),base)


print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False
print(is_power_of(68,5))
print(is_power_of(68,4))
print(is_power_of(500,5)) 
