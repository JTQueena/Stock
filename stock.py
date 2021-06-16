import twstock
import time
for key in [1326, 2887, 3450, 5880]:
    key = str(key)
    stock = twstock.Stock(key)
    day5avg = stock.moving_average(stock.price, 5)
    day10avg = stock.moving_average(stock.price, 10)
    day30avg = stock.moving_average(stock.price, 30)
    fStockPrice = float(stock.price[-1])
    fDay5avg = float(day5avg[-1])
    fDay10avg = float(day10avg[-1])
    fDay30avg = float(day30avg[-1])
    buySellMA5 = "BUY" if fStockPrice > fDay5avg else "SELL"
    buySellMA10 = "BUY" if fStockPrice > fDay10avg else "SELL"
    buySellMA30 = "BUY" if fStockPrice > fDay30avg else "SELL"
    print("-----", stock.sid, "-----")
    '''
    print("Pnow", stock.price[-1])
    print("MA 5", day5avg[-1], buySellMA5)
    print("MA10", day10avg[-1], buySellMA10)
    print("MA30", day30avg[-1], buySellMA30)
    '''
    print(f"Pnow: {fStockPrice:<6.2f}")
    print(f"MA 5: {fDay5avg:<6.2f} {buySellMA5:<5s}")
    print(f"MA10: {fDay10avg:<6.2f} {buySellMA10:<5s}")
    print(f"MA30: {fDay30avg:<6.2f} {buySellMA30:<5s}")
    time.sleep(10)