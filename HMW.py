 Make a simple function called greet that returns the most-famous "hello world!".

 def greet():
     return "hello world!"

 https://www.codewars.com/kata/523b4ff7adca849afe000035/solutions/python?filter=me&sort=best_practice&invalids=false


We need a function that can transform a string into a number. What ways of achieving this do you know?

def string_to_number(s):
    return int(s)

https://www.codewars.com/kata/544675c6f971f7399a000e79/solutions?filter=me&sort=best_practice&invalids=false


Complete the square sum function so that it squares each number passed into it and then sums the results together.

def square_sum(numbers):
    total = 0
    for num in numbers:
        total += num ** 2
        
    return total

https://www.codewars.com/kata/515e271a311df0350d00000f/solutions/python?filter=me&sort=best_practice&invalids=false


def quotable(name, quote):
    return f'{name} said: "{quote}"'

https://www.codewars.com/kata/5859c82bd41fc6207900007a/solutions/python?filter=me&sort=best_practice&invalids=false



def agents(list_found, list_records):
    if not list_found : return None
    if list_found in list_records : return 'Match found'
    else: return 'No matches'

https://www.codewars.com/kata/5a5bef7a5c770d08cd0032fa/solutions/python?filter=me&sort=best_practice&invalids=false