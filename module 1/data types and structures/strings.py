def double_word(word):
    legnth = word *2
    legnth += str(len(legnth))
    return legnth

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

def first_and_last(message):
    if len(message) == 0:
     return False
    elif message[0] == message[-1]:
      return True
    else:
      return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))
