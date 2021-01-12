'''
Create a class named 'Electric' which is a subclass of 'Car'.

Constructor:
The constructor should accept all of the parameters the constructor of 'Car' needs as well as a parameter for battery size.
The constructor should call the constructor for Car to setup a generic car, then setup fields for batt_size (initialize appropriately) and charge_level (initialize to 100)

Methods:
Create a method 'drive' where, if the charge level is high enough, will print a message saying the car is driving and reduce the charge level by an appropriate amount.  Print an alert message if the battery runs out of charge.

Create a method 'recharge' which fully recharges the battery and prints an appropriate message.

Create a method 'honk_horn' which honks the horn.

Create a __str__ method which calls the __str__ method in Car and appends the charge level on the end.
'''
