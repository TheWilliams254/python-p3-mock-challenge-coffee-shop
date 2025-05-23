class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) < 4:
            raise Exception("Name must be at least 4 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # raise Exception("Cannot change coffee name")
        if hasattr(self, '_name'):
            raise Exception("Cannot change coffee name")
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 4:
            raise Exception("Name must be at least 4 characters")
        self._name = value

    def orders(self):
        """return all orders for this coffee"""
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        return list(set(order.customer for order in self.orders()))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        return sum(order.price for order in orders) / len(orders) if orders else 0


class Customer:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if not 3 <= len(name) <= 15:
            raise Exception("Name must be between 3 and 15 characters")
        self._name = name
        Customer._all.append(self)

    @property
    def name(self):        
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if not 3 <= len(value) <= 15:
            raise Exception("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        return list(set(order.coffee for order in self.orders()))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise Exception("Must be a Coffee instance")
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        if not isinstance(coffee, Coffee):
            raise Exception("Must be a Coffee instance")
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending.items(), key=lambda x: x[1])[0] if customer_spending else None


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise Exception("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise Exception("Coffee must be a Coffee instance")
        if not isinstance(price, (int, float)) or not 1.0 <= float(price) <= 10.0:
            raise Exception("Price must be a number between 1.0 and 10.0")
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        raise Exception("Cannot change price")

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee