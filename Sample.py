#! c:\python\bin

# print("Hello World")
# print("Hello World")

# this is a comment
print("Hello World") # this is a comment
print("Hello World")
print("Hello World")
"""
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
"""

print("-" * 60)

def fun():
    # function code   - single indentation
    for i in range(1, 11):
        # for loop code
        if i % 2 == 1:
            # if condition code
            print('Hello World')

        # print 'for loop code' - every iteration
        print(f"for loop {i}")

    # function code - once
    print('Function code.....')

fun()