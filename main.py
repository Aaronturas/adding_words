#You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
#The function should be able to take a varying number of words as the argument.

def concatenate(*args):
    new_str = []
    for i in args:
        new_str += (i +'-')
    new_str.pop()
    new_str =''.join(new_str)
    return new_str

#Testcases
print(concatenate("I", "love", "Python", "!\n"))

print(concatenate("This", "is", "Great", "!"))