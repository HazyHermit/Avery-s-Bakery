Hazelle Malonzo 
2 December 2021 
CSE 20 
Assignment 10.1 - Your Own Class 

	Welcome to Avery's bakery, a demo program with a single class that models after a regular bakery. This bakery has several treats with different prices, and the user can store, add, and remove baked goods to their order, which will ultimately change the total price. They can increase or decrease quantities of a single treat. It's pretty much similar to a regular simple bakery.


VARIABLES
Class Variable: 
	treat_menu - this class variable handles a properly formatted menu for the bakery. It is called in the menu() method. 
 
Data Variables:
	self.__treats - this is basically the menu, but it is placed in a dictionary with its respective prices. 
	self.__order - this dictionary is the user's order in which they will store, add, or remove treats. 


METHODS 
def __init__(self, order = none): 
	This is a basic constructor method that contains self.__treats and self.__order. At first, the order is set to none as default if the user does not input an argument. If the user decides to add something in the argument, such as a dictionary of their order ({treat:quantity}), then this method will return the order's receipt, which is the self.cart_total() method.

def treat_price(self, treat): 
	The treat_price method returns the price of the treat given inside of the argument. It only takes one argument at a time. 

def cart_total(self): 
	This method returns the total price of the user's order without much formatting. It is also used in relation to other methods such as add_treats / remove_treats and the __str__ method. 

def add_treats / remove_treats (self, treat, count): 
	This method takes in two arguments: the name of the treat and the number of treats in which the user wants to add or remove from their order. This method changes the price of the order depending on what is added or removed, and returns the receipt at the end of the method. 

def __str__(self): 
	This method just reformats the information of self.__order and returns a receipt of the bakery order. 

def menu(self): 
	This returns the ony class variable in the program, which is the menu containing the treats and their prices. 


DEMO PROGRAM DOCUMENTATION 

What happens in Avery's Bakery?
	In this demo program, the user can include as many treats as they want in a dictionary format. Then, the program will return a receipt of the total cost of the entire order. 

How does Avery's Bakery work? 
	Like a simple bakery, the user can input their order in the testcart variable, preferrably in a dictionary format ({name of treat: number of treat}). An example should already be provided in the main function. The program should then return the order back to them, along with the total cost. There are other methods displayed in which they can change up their order, adding or removing items from it. It is more or less similar to how the fruit basket works.   

 

