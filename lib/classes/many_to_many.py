class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 3:
            raise Exception("Name must be at least 3 characters")
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed")
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 3:
            raise Exception("Name must be at least 3 characters")
        self._name = name
    def orders(self):
        return [order.customer for order in Order.all if order.coffee == self]

        pass
    
    def customers(self):
        return (set(order.customer for order in self.orders()))

        pass
    
    def num_orders(self):
        return len(self.orders())
        pass
    
    def average_price(self):
        return sum(order.price for order in self.orders()) / len(self.orders()) if self.orders() else 0
        pass

class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 3 <= len(name) <= 15:
            raise Exception("Name must be between 3 and 15 characters")
        self.name = name
        Customer.all.append(self)
        
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise Exception("Name cannot be changed")
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 3 <= len(name) <= 15:
            raise Exception("Name must be between 3 and 15 characters")
        self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
        pass
    
    def coffees(self):
        return (set(order.coffee for order in self.orders()))
        pass
    
    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of Coffee")
        if not isinstance(price, float):
            raise Exception("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise Exception("Price must be between 1.0 and 10.0")
        order = Order(self, coffee, price)
        Order.all.append(order)
        return order
        pass
    @classmethod
    def get_all(cls):
        return cls.all
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be an instance of Coffee")
        if not isinstance(price, float):
            raise Exception("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise Exception("Price must be between 1.0 and 10.0")
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
         return self._price

    @price.setter
    def price(self, price):
        if not isinstance(price, float):
            raise Exception("Price must be a float")
        if not 1.0 <= price <= 10.0:
            raise Exception("Price must be between 1.0 and 10.0")
        self._price = price

        pass

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be an instance of Customer")
        self._customer = customer