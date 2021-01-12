'''
Create a class named 'ICE' which is a subclass of 'Car'.

Constructor:
The constructor should accept all of the parameters the constructor of 'Car' needs as well as a parameter for fuel tank capacity.
The constructor should call the constructor for Car to setup a generic car, then setup fields for fuel tank capacity (initialize appropriately) and fuel level (initialize to something that makes sense)

Methods:
Create a method 'drive' where, if the fuel level is high enough, will print a message saying the car is driving and reduce the fuel level by an appropriate amount.  Print an alert message if the tank runs out of gas.

Create a method 'refuel' which fully refuels the tank and prints an appropriate message.

Create a method 'honk_horn' which honks the horn.

Create a __str__ method which calls the __str__ method in Car and appends the fuel level on the end.
'''
