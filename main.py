
from OrderBook.OrderBook import OrderBook
from OrderBook.Order import Order
# Initialize the Order Book
lob = OrderBook()

# LMT - Limit Order, MKT - Market Order,

# Adding some Limit orders
ordr1 = Order("LMT", "BUY", 200, 33.71)
ordr2 = Order("LMT", "BUY", 100, 33.78)
ordr3 = Order("LMT", "BUY", 500, 33.74)
ordr6 = Order("LMT", "BUY", 200, 33.78)

ordr4 = Order("LMT", "SELL", 200, 33.78)
ordr5 = Order("LMT", "SELL", 500, 33.74)

lob.processOrder(ordr1)
lob.processOrder(ordr2)
lob.processOrder(ordr3)
lob.processOrder(ordr4)
lob.processOrder(ordr5)
lob.processOrder(ordr6)

# printing order book
print(lob)
print("------------------------------------\n")
# printing Best Bid and Offer (Ask)
print("BBO:", lob.getBBO())

# Adding some Market Orders
mordr1 = Order("MKT", "BUY", 400)
mordr2 = Order("MKT", "SELL", 500)

lob.processOrder(mordr1)
lob.processOrder(mordr2)

print(lob)

# Adding Stop Orders
