"""
Title:
Can we divide it?

Description:
Your task is to create functionisDivideBy (or is_divide_by) to check if an integer number is divisible by each out of two arguments.

Link: https://www.codewars.com/kata/5a2b703dc5e2845c0900005a
"""

def is_divide_by(number, a, b):
  if number % a == 0 and number % b == 0:
    return True
  else:
    return False


if __name__ == '__main__':
  number = 2
  a = 10
  b = 3

  result = is_divide_by(number, a, b)
  print(result)