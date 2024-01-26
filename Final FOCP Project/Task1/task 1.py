def pizza_calc(npizza,delivery='n',tuesday='n', app='n'):
    
    '''Calculates the total price
       npizza:number of pizza
       delivery:home delivery flag
       tuesday:tuesday discount flag
       app:Order from app flag'''
    
    Avg_cost = 12.0 #Pizza cost
    delivery_cost=0
    price=(npizza*Avg_cost) 
   
    if delivery =='y'or delivery =='yes':  #check if customer wants home delivery
        delivery_cost=2.5
        if npizza>=5:      #delivery charge 0 if pizzas is more than 4
            delivery_cost=0 
     

    if tuesday =='y' or tuesday =='yes': #check if it is tuesday
       tuesday_price = price*0.5    #apply discount if true
    else:
        tuesday_price = price   

    if app =='y' or app =='yes':     #check if ordered from app
        app_price = tuesday_price*0.75
    else:
        app_price = tuesday_price 
        
    delivery_price = delivery_cost+app_price  #calculate final cost 
    return round(delivery_price, 2),app_price, tuesday_price, price   #round off to 2 decimal place

#exception and error handling
def check_count(): 
    while True:
        try:
            npizza = int(input("How many pizzas ordered? "))
            if npizza < 0:
                raise ValueError("Number of pizzas should be a positive integer.")
            return npizza
        except ValueError:
            print("Error: Please provide a valid number for the number of pizzas.")

def check_deliv():
    while True:
        delivery = input("Is delivery required? ").lower()
        if delivery == 'y' or delivery == 'yes' or delivery == 'n' or delivery == 'no':
            return delivery
        else:
            print("Error: Please provide 'y' or 'n' for the delivery option.")

def check_day():
    while True:
        tuesday = input("Is it Tuesday? ").lower()
        if tuesday == 'y' or tuesday == 'yes' or tuesday == 'n' or tuesday == 'no':
            return tuesday
        else:
            print("Error: Please provide 'y' or 'n' for the Tuesday discount flag.")

def check_app():
    while True:
        app = input("Did the customer use the app? ").lower()
        if app == 'y' or app == 'yes' or app == 'n' or app == 'no':
            return app
        else:
            print("Error: Please provide 'y' or 'n' for the app flag.")

#Main calculator

# Main loop          
while True:
    print("BPP Pizza Price Calculator")
    print("==========================\n")
    npizza = check_count()
    delivery = check_deliv()
    tuesday = check_day()
    app = check_app()
    
    final_price, app_price, tuesday_price, price = pizza_calc(npizza, delivery, tuesday, app)
    tuesday_discount = price - tuesday_price
    app_discount = tuesday_price - app_price
    delivery_fee = final_price - app_price
    
    print("Tuesday Discount: £", tuesday_discount)
    print("App Discount: £", app_discount)
    print("Delivery Fee: £", delivery_fee)
    print("Total Price: £", final_price)
    further = input("\nCalculate next order? ")
    if further=='n':
        break