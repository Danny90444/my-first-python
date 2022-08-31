def double_word(word):
    legnth = word *2
    legnth += str(len(legnth))
    return legnth

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

def first_and_last(message):
    if message:
        return message[0] == message [-1]
    return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))


def first_and_last(message):
    if message:
        return message[0] == message[-1]
    return True

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last("A"))
print(first_and_last(""))

def initials(phrase):
  words = phrase.split()
  result = ""
  for word in words:
    result += word[0].upper()
  return result

print(initials("Universal Serial Bus"))

def student_grade(name, grade):
	print("{} received {}% on the exam.".format(name,grade))
	return ""

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

print("test")