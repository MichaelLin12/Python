# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


simple = my_gen()
print(next(simple))
print(next(simple))
print(next(simple))


def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1, -1, -1):
        yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
    print(char)


my_list = [1, 3, 6, 10]
generator = (x**2 for x in my_list)
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))


# Generator expressions can be used as function arguments. 
# When used in such a way, the round parentheses can be dropped.


print(sum(x**2 for x in my_list))
print(max(x**2 for x in my_list))


def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))