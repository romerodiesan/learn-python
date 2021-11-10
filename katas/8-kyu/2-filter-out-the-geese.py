"""
Title:
Filter out the geese

Description:
Write a function, gooseFilter / goose-filter / goose_filter / GooseFilter, that takes an array of strings as an argument and returns a filtered array containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

Link: https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/
"""


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
  elements = filter(lambda x : x not in geese, birds)
  elements = list(elements)
  return elements


if __name__ == '__main__':
  elements = ["African", "Miami", "LittleBird", "Pilgrim"]
  print(goose_filter(elements))