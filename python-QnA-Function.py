'''
Question: Write a Python function that accepts a string and counts the number of upper and
lower case letters.
'''

def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for  char in string:
      if char.isupper():
          upper_count +=1
      elif char.islower():
          lower_count +=1

    return upper_count, lower_count

input_string = "Welcome to learn DevOps & Cloud Engineering"
upper, lower = count_upper_lower(input_string)

print(f"UPPER CASE LATTERS:{upper}")
print(f"LOWER CASE LATERS:{lower}")


'''

Write a Python function that takes a list and returns a new list with distinct
elements from the first list.
input_list = [1, 2, 2, 3, 4, 4, 5]
output_list: [1, 2, 3, 4, 5]
'''

def distinc_list(input_list):
    return list (set(input_list))

input_list = [1,2,2,3,4,4,5]
output_list = distinc_list(input_list)
print(output_list)


'''ArithmeticError3] Write a Python function that takes a number as a parameter and checks whether the
number is prime or not.'''

def is_prime(number):
      if number <= 1:
          return False
      for i in range (2, int(number**0.5) + 1):
          if number % 1== 0:
              return False
          return True 
num = 29
if is_prime(num):
    print(f"{num}is a prime number")
else:
    print(f"{num}is not a prime number")


'''Write a Python function that takes a list of numbers and prints the even numbers
from the list.'''


def print_even_number(numbers):
    for number in numbers:
        if number % 2 == 0 :
            print(number)

Numbers_List = [1,2,3,4,5,6,7,8,9,10,11,12]
print_even_number(Numbers_List)


'''5] Write a Python function that checks whether a passed string is a palindrome or
not.'''

def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:  # Check if the number is even
            print(number)

# Example usage
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8]
print_even_numbers(numbers_list)


'''8] Write a Python function that calculates the length of a given list'''

def list_lenght(lst):
    return len(lst)

new_list = [1,2,3,4,5,6,7,8,9]
lenght =list_lenght(new_list)
print(f"The Lenght Of The List is:{len}")


'''
9.  Write a Python function that takes two numbers as parameters and returns the
maximum of the two.
'''

def new_max(n1, n2):
    return max(n1, n2)

result = new_max(100, 200)
print(f"The MAX NO IS: {result}")

def list_max(num1, num2):
    return max(num1, num2)
result  = list_max(1,2)
print(result)

'''
10] Write a Python function that takes two numbers as parameters and returns the
# minimum of the two:
'''
def get_min(num1, num2):
    return min (num1, num2)
result = get_min(10, 20)
print(result)

'''11] Write a Python function that takes a string as input, splits the string into words,
reverses the order of words, and returns the reversed string.'''
# not understand
def reverse_words(input_string):
    # Split the string into words
    words = input_string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed list of words back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Example usage
input_str = "Hello world this is Python"
reversed_str = reverse_words(input_str)
print(f"Reversed string: '{reversed_str}'")
