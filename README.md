# Limit Order Book (Python Implementation)

## Introduction
This project is an implementaion of limit order book in python.
We can enter Limit and Market orders in the book by creating a Order() object and
passing arguments as Order(order_type, direction, size, price)

* <b>order_type</b>: It is the order type (Limit Order, Market Order) supplied as string ("LMT", "MKT").
* <b>direction</b>: It is the type of Order (Buy or Sell) supplied as string ("BUY", "SELL").
* <b>size</b>: It is the size of Order supplied as any non-negative integer.
* <b>price</b>: It is an optional parameter, only used for Limit Orders.

## How to use
* Run `python main.py` to run examples.

## References
* Richard Holowczak's explaination on Limit Order Books [Youtube](https://www.youtube.com/watch?v=Iaiw5iGjXbw)
* 5minutefinance article [5minutefinance](https://www.5minutefinance.org/concepts/the-limit-order-book)