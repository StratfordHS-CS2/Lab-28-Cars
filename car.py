'''
This is the class that defines a generic Car.
'''

class Car:
  def __init__(self, make='', model='', year=''):
    self.make = make
    self.model = model
    self.year = year
  
  def drive(self):
    print("The car is driving")

  def __str__(self):
    return 'This is a ' + self.year + ' ' + self.make + ' ' + self.model