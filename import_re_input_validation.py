import re  # python module for 'regular expressions'
# use 'regular expressions' to validate input
# 'regular expressions' looks for patterns in strings or text
# can be used as an alternative to if statements

# LOOKS FOR AN UPPERCASE WORD
pattern = re.compile("^[A-Z]+$")  # compiles a pattern with all uppercase words
# ' ^ ' represents the start of the whole string of a pattern
# ' + ' represents that a character can occur at least once
# ' $ ' represents the end of the string in the pattern
# the parameter says the whole string can only have whats inside (^ [???] +$)

print(pattern.search("Hello World"))  # '.search' looks into the whole string
print(pattern.search("HELLO WORLD"))
print(pattern.search("HELLOWORLD"))
print(pattern.match("Hello World"))  # '.match' looks if it start with the criteria
print()

# LOOKS FOR ABC
test_string = '123abc456def789'

new_pattern = re.compile(r"abc")  # looks for abc
# 'r' indicates the beginning of a raw string
matches = new_pattern.finditer(test_string)  # '.finditer' locates the positions of the matches

matches1 = re.finditer(r"abc", test_string)  # an alternative way to do same as above

matches2 = new_pattern.match(test_string)  # '.match' determines if the beginning matches

for match in matches:
    print(match)
print()


# LOOKS FOR AN UPPERCASE LETTER
pattern1 = re.compile("[A-Z]+")  # compiles a pattern with an uppercase letter

print(pattern1.search("Hello World"))
print(pattern1.search("HELLO WORLD"))
print(pattern1.search("HELLOWORLD"))
print()


# LOOKS FOR AN UPPERCASE AND LOWERCASE LETTERS AND SPACES
pattern2 = re.compile("^[a-zA-Z\s]+$")  # compiles a pattern with all uppercase words
# ' \s ' looks for spaces


# LOOKS FOR 3 LOWERCASE LETTERS, 3-5 DIGITS, ONE SYMBOL, UP TO UPPERCASE LETTERS
pattern3 = re.compile("^[a-z]{3}[0-9]{3,5}[^a-zA-Z0-9]{1}[A-Z]{0,2}$")

# ' [a-z]{3} ' means to have 3 lowercase letters
# ' [0-9]{3,5} ' means 3-5 between 0-9 are allowed
# ' [^a-zA-Z0-9]{1} ' means NOT all of this so YES to symbols at least once
# ' [A-Z]{0,2} ' means 0-2 uppercase letters are allowed


# LOOKS FOR ANY CHARACTER 10 TIMES
pattern4 = re.compile("^.{10}$")
# ' .{10} ' means anything 10 times


# LOOKS FOR AN EMAIL ADDRESS
pattern5 = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern5.search("nine@gmail.com"))
print(pattern5.search("nine3@gmail.com"))
print(pattern5.search("nine-gmail.com"))
print()


# USES FINDALL
pattern6 = "Hey I love GOD so much. GOD is literally the greatest"
print(re.findall("GOD", pattern6))  # finds the word and prints it as many times as used
print(re.search("GOD", pattern6))  # prints the location of the word


# SPECIAL CHARACTERS
# ' \d ' matches any decimal digit
# ' \D ' matches any non-digit character
# ' \w ' matches any alphanumeric (word) character; [a-zA-Z0-9_]
# ' \W ' matches any non alphanumeric character
# ' \b ' matches where the specified characters are at the beginning or at the end of a word
    # ex: r"\bain" r"ain\b"
# ' \B ' matches where the specified characters are present, but not at the beginning


# NOTES
# one of the differences between findall, matches, compile, search, etc is the output





