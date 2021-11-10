"""
Title:
Keep Hydrated!

Description:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

Link: https://www.codewars.com/kata/582cb0224e56e068d800003c
"""
import math

def litres(time):
  result = math.floor(time / 2)
  return result


if __name__ == '__main__':
  time = 10
  quantity = litres(time) 

  print(quantity)