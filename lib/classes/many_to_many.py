class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, '_name'):
            raise Exception("Coffee already has a name and it can't be changed")
        elif isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string and equal to or greater than 3 characters")

        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        unique_customers = {order.customer for order in self.orders()}
        return list(unique_customers)
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        total_price = sum([order.price for order in self.orders()])
        return total_price / len(self.orders())

class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError("Name must be a string and between 1 and 15 characters")
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_coffees = {order.coffee for order in self.orders()}
        return list(unique_coffees)
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        if hasattr(self, '_price'):
            raise Exception("Price can not be changed")
        elif isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("Price must be a float and between 1.0 and 10.0")
    
    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instnace of the Customer class")
        else:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of the Coffee class")
        else:
            self._coffee = coffee