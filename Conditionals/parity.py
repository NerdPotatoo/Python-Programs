#1
# num = int(input("What's num? "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#2
# def main():
#     num = int(input("What's num? "))
#     if is_even(num):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# main()

#3
# def main():
#     num = int(input("What's num? "))
#     if is_even(num):
#         print("Even")
#     else:
#         print("Odd")

# def is_even(n):
#     return True if n % 2 == 0 else False 
    
# main()

#4
def main():
    num = int(input("What's num? "))
    if is_even(num):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return n % 2 == 0 
    
main()