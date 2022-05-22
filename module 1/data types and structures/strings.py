def double_word(word):
    legnth = word *2
    legnth += str(len(legnth))
    return legnth

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
