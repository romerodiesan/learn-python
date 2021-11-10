"""
Title:
Reversed String

Description:
Complete the solution so that it reverses the string passed into it.

Link:
https://www.codewars.com/kata/5168bb5dfe9a00b126000018
"""

def reversed_string(string):
  return string[::-1]


if __name__ == '__main__':
  word = 'amor'

  print(reversed_string(word))