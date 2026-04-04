# Documentation for python here: //docs.python.org//

#1
#print("Hello, World")

#2
#input("What's your name? ")
#print("Hello, Sami")

#3
#name = input("Whats your name? ")
#print("hello,",name)

#4
#name = input("Whats your name? ")
#print("hello, " + name)

#From Doc
#print(*objects, sep = '', end = '\n')

#5
#name = input("What's your name? ")
#print("Hello, ", end = "")
#print(name)


#name = input("What's your name? ")
#print("Hello, ", name, sep = "")

#6
# print('hello, "Friend"')
# print("Hello, \"friend\"")

#7
#name = input("What's your name? ")
#print("Hello, {name}")
#print(f"Hello, {name}")

#8
# name = input("What's your name? ")

#remove whitespace from str
#name = name.strip()

#Capatalize user's name
#name = name.capitalize()

#capatilaze user's name 
#name = name.title()

# All these together 
#name = name.strip().title()
#name = input("What's your name? ").strip().title()

#print(f"Hello, {name}")

#9
#name = input("What's your name? ").strip().title()

#first , last = name.split(" ")
#print(f"Hello, {last}")

### 10 def ###
#def hello():
#    print("hello")

#name = input("What's yout name? ")
#hello()
#print(name)

### 11 ###
#def hello(to):
#    print("hello", to)

#name = input("What's yout name? ")
#hello(name)

### 11 ###
#def hello(to ="World"):
#    print("hello", to)

#hello()
#name = input("What's yout name? ").title()
#hello(name)

### 12 ###
#def main():
#    name = input("What's yout name? ").title()
#    hello(name)

#def hello(to):
#    print("hello", to)

#main()