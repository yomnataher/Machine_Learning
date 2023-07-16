print("Hello world")

a=10
print(a)

#############################################
t = True
f = False
print(type(t))
print(t and f)
print(t or f)
print(not t)
print(t != f)

#############################################
hello = 'Hello'
world = 'World'
print(hello)
print(len(hello))
hw = hello + ' ' + world
print(hw + "!")


hw12= '%s %s %d'% (hello , world , 12)
print(hw12)



course = 'Machine learning'
print(course[0])
print(course[5])
print(course[-1])
print(course[1:3])
print(course[1:])
print(course[:6])
#################################################

name = 'Mohammed'
message = f'Hi, my name is {name}'
print(message.upper())# to convert to uppercase
print(message.lower()) # to convert to lowercase
print(message.title()) # to capitalize the first letter of every word
print(message.find('o')) # returns the index of the first occurrence of p (or -1 if notfound)
print(message.replace('o', 'q'))
#################################################


from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
# generate regression dataset
X, y = make_regression(n_samples=100, n_features=1, noise=3.2)
# plot regression dataset
print(plt.scatter(X,y))
print(plt.show())
