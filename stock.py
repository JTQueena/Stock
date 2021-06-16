import twstock
import time
for key in [1326, 2887, 3450, 5880]:
    key = str(key)
    stock = twstock.Stock(key)
    day5avg = stock.moving_average(stock.price, 5)
    day10avg = stock.moving_average(stock.price, 10)
    day30avg = stock.moving_average(stock.price, 30)
    print("-----", stock.sid, "-----")
    print("MA 5", day5avg[-1])
    print("MA10", day10avg[-1])
    print("MA30", day30avg[-1])
    time.sleep(10)
