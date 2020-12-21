# creating variable x that contains format character
x = "There are %d types of people." % 10

# creating variable binary
binary = "binary"

# creating variable do_not
do_not = "don't"

# creating variable y, contains format character
y = "Those who know %s and those who %s." % (binary, do_not)

# printing content of variable x
print(x)

# printing content of variable y
print(y)

# printing the content of variable x
print("I said: %r." % x)

# printing the content of variable y
print("I also said: '%s'." % y)

# creating variable with boolean content
hilarious = True

# creating variable, contains format character
joke_evaluation = "Isn't that joke so funny?! %r"

# printing combination of two variables
print(joke_evaluation % hilarious)

# creating variable w with string content
w = "This is the left side of..."

# variable e, the content is string as well
e = "a string with a right side."

# printing both variable w and e, consist of strings
print(w + e)
