import twstock
import time
for key in [1326, 2887, 3450, 5880, 2330, 9958, 2108, 2382, 2884, 1795]:
    key = str(key)
    stock = twstock.Stock(key)
    time.sleep(3)
    day5avg = stock.moving_average(stock.price, 5)
    time.sleep(3)
    day10avg = stock.moving_average(stock.price, 10)
    time.sleep(3)
    day30avg = stock.moving_average(stock.price, 30)
    time.sleep(3)
    fStockPrice = float(stock.price[-1])
    time.sleep(3)
    fDay5avg = float(day5avg[-1])
    fDay10avg = float(day10avg[-1])
    fDay30avg = float(day30avg[-1])
    buySellMA5 = "BUY" if fStockPrice > fDay5avg else "SELL"
    buySellMA10 = "BUY" if fStockPrice > fDay10avg else "SELL"
    buySellMA30 = "BUY" if fStockPrice > fDay30avg else "SELL"
    openfile = open("stockMA.txt", mode="a")
    print("-----", stock.sid, "-----", file=openfile)
    time.sleep(3)
    print(f"Pnow: {fStockPrice:<6.2f}", file=openfile)
    print(f"MA 5: {fDay5avg:<6.2f} {buySellMA5:<5s}", file=openfile)
    print(f"MA10: {fDay10avg:<6.2f} {buySellMA10:<5s}", file=openfile)
    print(f"MA30: {fDay30avg:<6.2f} {buySellMA30:<5s}", file=openfile)
    openfile.close()
    time.sleep(5)
print("DONE")
