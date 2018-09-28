#OOPR-Assgn-18
#Start writing your code here
class Customer:
    def __init__(self,customer_name):
        self.__customer_name=customer_name
        self.__payment_status=None

    def get_customer_name(self):
        return self.__customer_name
    def get_payment_status(self):
        return self.__payment_status
    
    def pays_bill(self,bill):
        self.__payment_status="Paid"
        
    


class Bill:
    counter=1000
    
    def __init__(self):
        self.__bill_id=None
        self.__bill_amount=None

    def get_bill_id(self):
        return self.__bill_id
    def get_bill_amount(self):
        return self.__bill_amount

    def generate_bill_amount(self,item_quantity,items):
        self.__bill_amount=0
        for x,y in item_quantity.items():
            for i in range(0,len(items)):
                id1=items[i].get_item_id()
                if(x.lower()==id1.lower()):
                    self.__bill_amount+=items[i].get_price_per_quantity()*y
        Bill.counter+=1
        self.__bill_id="B"+str(Bill.counter)
            
    
class Item:
    def __init__(self,item_id,description,price_per_quantity):
        self.__item_id=item_id
        self.__description=description
        self.__price_per_quantity=price_per_quantity

    def get_item_id(self):
        return self.__item_id
    def get_description(self):
        return self.__description
    def get_price_per_quantity(self):
        return self.__price_per_quantity

    