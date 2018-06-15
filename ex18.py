 This one is like your scripts with argv 

def print_two(*args):
	arg1, arg2 = args 
	print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok, that *args is actually pointless, we can just do this.

def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument.
def print_one(arg1):
	print "arg1: %r" % arg1 

# this ine takes one arguments.
def print_none():
	print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()



# First we tell Python we want to make a function def for define.
# On the same line as def, we just called it print_two, but it could be peanuts too. 
# It doesn't matter, except that your function should have a short name that says what it does.



# On the same line as def, we then give the function a name. In this case, we just called it print_two,
# but it could be peanuts too. It doesn't matter, except that your function should have a short
# name that says what it does.

# Then we tell it we want *args (asterisk args), which is a lot like your argv parameter but functions 
# This a lot like your argv parameter but for functions. This has to go inside() parentheses to work.

# Then we end this line with a : colon and start indenting.

# After the colon all the lines that are indented four spaces willl become 
# attached to this name, print_two. Our first indented line is one that unpacks the 
# arguments the same as with your scripts.

# To demonstrate how it works we print these arguments out, 
# just like we would in a script.

 
	
