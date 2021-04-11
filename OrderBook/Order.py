class Order:
    def __init__(self, order_type, direction, size, price = 0):
        self.order_type = order_type
        self.size = size
        self.price = price
        self.direction = direction
