def getOrderKey(order):
    return float(order.price)


class OrderBook:
    def __init__(self):
        self.bid = []
        self.ask = []

    def processOrder(self, order):
        if order.order_type == "LMT":
            self.limitOrder(order)
        if order.order_type == "MKT":
            pass

    def limitOrder(self, order):
        if order.direction == "BUY":
            self.bid.append(order)
            self.bid.sort(key=getOrderKey, reverse=True)
        else:
            self.ask.append(order)
            self.ask.sort(key=getOrderKey)

    def getBBO(self):
        return f"Bid/Ask: {self.bid[0].price}/{self.ask[0].price}\n"

    def isEmpty(self):
        return len(self.bid) == 0 and len(self.ask) == 0

    def __str__(self):
        if self.isEmpty():
            return "Order Book is Empty"
        else:
            print_str = "Bid Size\tBid Price\n"
            print_str += "--------------------\n"
            for order in self.bid:
                print_str += f"{order.size}\t\t${order.price}\n"

            print_str += "\nAsk Size\tAsk Price\n"
            print_str += "--------------------\n"
            for order in self.ask:
                print_str += f"{order.size}\t\t${order.price}\n"
            return print_str
