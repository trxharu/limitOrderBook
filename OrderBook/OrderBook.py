import sys


def getOrderKey(order):
    return order.price


class OrderBook:
    def __init__(self):
        self.bid = []
        self.ask = []

    def processOrder(self, order):
        if order.order_type == "LMT":
            self.limitOrder(order)
        elif order.order_type == "MKT":
            self.marketOrder(order)
        else:
            print("Error: Order type is invalid. Must be of (LMT, MKT, STP)")
            sys.exit(-1)

    def limitOrder(self, order):
        if order.size < 0:
            print("Error: Order size cannot be negative")
            sys.exit(-1)
        if order.price < 0:
            print("Error: Order price cannot be negative")
            sys.exit(-1)

        if order.direction == "BUY":
            self.bid.append(order)
            self.bid.sort(key=getOrderKey, reverse=True)
        elif order.direction == "SELL":
            self.ask.append(order)
            self.ask.sort(key=getOrderKey)
        else:
            print("Error: Order Direction is invalid. Must be of (BUY or SELL)")
            sys.exit(-1)

    def marketOrder(self, mktorder):
        if mktorder.direction == "BUY" and len(self.ask) != 0:
            mkt_order_size = mktorder.size
            while mkt_order_size > 0 and len(self.ask) != 0:
                order = self.ask.pop(0)
                if order.size > mkt_order_size:
                    order.size -= mkt_order_size
                    self.ask.insert(0, order)
                    break
                else:
                    mkt_order_size -= order.size
        elif mktorder.direction == "SELL" and len(self.bid) != 0:
            mkt_order_size = mktorder.size
            while mkt_order_size > 0 and len(self.bid) != 0:
                order = self.bid.pop(0)
                if order.size > mkt_order_size:
                    order.size -= mkt_order_size
                    self.bid.insert(0, order)
                    break
                else:
                    mkt_order_size -= order.size
        else:
            print("Error: Order Direction is invalid. Must be of (BUY or SELL)")
            sys.exit(-1)

    def getBBO(self):
        if not self.isEmpty():
            return f"Bid/Ask - {self.bid[0].price}/{self.ask[0].price}\n"
        else:
            return "Order Book is empty"

    def isEmpty(self):
        return len(self.bid) == 0 and len(self.ask) == 0

    def __str__(self):
        if self.isEmpty():
            return "Order Book is Empty"
        else:
            print_str = "Time\tBidSize\tBidPrice\n"
            print_str += "------------------------------\n"
            for order in self.bid:
                print_str += f"{order.time}\t{order.size}\t\t${order.price}\n"

            print_str += "\nTime\tAskSize\tAskPrice\n"
            print_str += "------------------------------\n"
            for order in self.ask:
                print_str += f"{order.time}\t{order.size}\t\t${order.price}\n"
            return print_str
