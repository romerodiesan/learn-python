"""
Title:
Squash the bug

Link:
https://www.codewars.com/kata/56f173a35b91399a05000cb7

Description:
Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.
There will only be one 'longest' word.
"""

def find_longest(string):
  return max([len(word) for word in string.split()])


if __name__ == '__main__':
  longest = find_longest("hello world")
  print(longest)