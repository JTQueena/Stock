import twstock
import time
for key in [1326, 2887, 3450, 5880]:
    key = str(key)
    stock = twstock.Stock(key)
    day5avg = stock.moving_average(stock.price, 5)
    day10avg = stock.moving_average(stock.price, 10)
    day30avg = stock.moving_average(stock.price, 30)
    buySellMA5 = "BUY" if float(stock.price[-1]) > float(day5avg[-1]) else "SELL"
    buySellMA10 = "BUY" if float(stock.price[-1]) > float(day10avg[-1]) else "SELL"
    buySellMA30 = "BUY" if float(stock.price[-1]) > float(day30avg[-1]) else "SELL"
    print("-----", stock.sid, "-----")
    print("Pnow", stock.price[-1])
    print("MA 5", day5avg[-1], buySellMA5)
    print("MA10", day10avg[-1], buySellMA10)
    print("MA30", day30avg[-1], buySellMA30)
    time.sleep(10)
