"""Name: Hazelle Malonzo 
    Date: 30 November 2021
    Description: Assignment 10.1 - Avery's Bakery 

            Main Objective(s): 
                - model after a bakery with treats and a price for each treat 
                - user can add treats to their order along with their quantities 
                - program will calculate the total price of all treats and return a receipt of their order 
                - user can add and remove items from their order and it will change the total price 
                
                treats available: macarons, cookies, coffee cake, muffins, egg tarts 
                ** Add your treats in the main function below **
                """

class Bakery: 
    #USE OF CLASS VARIABLE: create menu for baked goods
    treat_menu = f"\t MENU \t \n macarons \t $6.00 \n cookies \t $2.00 \n coffee cake \t $5.00 \n muffins \t $3.00 \n egg tarts \t $2.00"

    #constructor method 
    def __init__(self, order=None):
        #create dictionary with treats and their prices (USE OF DATA VARIABLE)
        self.__treats = {'macarons':6.00 , 'cookies': 2.00 , 'coffee cake': 5.00 , 'muffins': 3.00, 'egg tarts': 2.00 }
        if order is None: 
            #intialize empty order (USE OF DATA VARIABLE)
            self.__order= {}
        else: 
            self.__order = {}
            #create for loop to count the amount of treats in the order
            for treats, count in order.items():
                self.__order[treats.lower()] = count 
        self.cart_total()

    #create treat_price method to return the price of a SINGLE treat (method only takes on one treat)
    def treat_price(self, treat):
        if treat in self.__treats: 
            return f'cost of {treat}: ${self.__treats.get(treat):.2f}'
        else: 
            print(f"Oops! {treat} is not on the menu. Please try again with the menu below.")
            print(self.menu())
            return None
    
    #create cart_total method to calculate the total cost of order 
    def cart_total(self):
        #intialize list for collecting total cost of each treat 
        total_cost = []
         #create for loop to count the amount of treats in the order
        for treats, count in self.__order.items():
            self.__order[treats.lower()] = count 
            #check if treat is in dictionary of treats 
            if treats in self.__treats: 
                #multiply the cost by the number of items in that one treat 
                 singlecost = self.__treats.get(treats) * count 
            total_cost.append(singlecost)
        return f'${sum(total_cost):.2f}'

    #create add/remove treats method to add and remove treats from order (SET- GET METHODS(2))
    def add_treats(self, treat, count): 
        #check if treat is in order
        if treat in self.__order.keys():
            #change quantity of treats added
            self.__order[treat.lower()] += count 
            return self.cart_total()
        else: 
            #if treat is not in order, add to order 
            self.__order[treat.lower()] = count 
            return self.cart_total()
    def remove_treats(self, treat, count): 
        #check if treat is in order
        if treat in self.__order.keys():
            self.__order[treat] -= count
            #if treat is less than 0, delete treat from order  
            if self.__order[treat] <= 0: 
                del self.__order[treat]
            return self.cart_total()
    

    #Create str method that prints out the receipt of the order 
    def __str__(self):
        display = ''
        #create for loop to reformat and remodel after a receipt
        for treat, count in self.__order.items():
            if treat in self.__treats: 
                cost = self.__treats.get(treat) * count 
            display += '\n' + str(treat) + f'({count}) \t ${cost:.2f}'
            display = ''.join(display)
        return (f"\t\n Here is your order: \t\n\t {display} \n ____________ \n Total: \t {self.cart_total()}") 
    
    #create menu method that returns a menu of baked goods 
    def menu(self): 
        #print menu (class variable) 
        # https://www.kite.com/python/answers/how-to-access-a-class-variable-from-a-class-method-in-python#:~:text=Use%20class_name.,class_name%20from%20a%20class%20method.
        print(Bakery.treat_menu)
        return ''


def main(): 

    #testing bakery order (enter the treats and number of treats like a dictionary)
    # ENTER YOUR ORDER HERE, IN DICTIONARY FORMAT ({TREAT:QUANTITY OF TREAT})
    testcart = Bakery({'macarons':5, 'coffee cake':1, 'muffins':8})

    #this prints the bakery's menu 
    print(testcart.menu())

    #testing receipt before adding changes to order 
    print(f"before changes: \n \t {testcart}")

    #testing the order's total cost 
    print(testcart.cart_total())

    #testing method that returns price of a certain treat 
    print(testcart.treat_price('macarons'))

    #testing add and remove method for treats 
    print(testcart.add_treats('coffee cake', 2))
    print(testcart.remove_treats('muffins', 4))

    #testing receipt after adding/removing changes 
    print(f"after change: \n {testcart}")


    

if __name__ == "__main__":
    main()
