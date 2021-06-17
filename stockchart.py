import twstock
import time
import matplotlib.pyplot as plt

for key in [1326, 2887, 3450, 5880]:
    key = str(key)
    stock2330 = twstock.Stock(key)
    
    # 此段為開發時獲取數據使用
    print(stock2330.price[-22:])
    print(stock2330.moving_average(stock2330.price, 5)[-22:])
    print(stock2330.moving_average(stock2330.price, 10)[-22:])
    # 此段為開發時獲取列表表度使用
    print(len(stock2330.price[-22:]))
    print(len(stock2330.moving_average(stock2330.price, 5)[-22:]))
    print(len(stock2330.moving_average(stock2330.price, 10)[-22:]))
    
    plt.title(stock2330.sid)
    plt.plot(stock2330.price[-22:], "r-", label="price")
    plt.plot(stock2330.moving_average(stock2330.price, 5)[-22:], "y-", label="MA 5")
    plt.plot(stock2330.moving_average(stock2330.price, 10)[-22:], "c-", label="MA10")
    plt.legend(loc="best")
    # 移動平均線顯示位置不對, 需再修正
    # 後來以[-22:]修正，以最短的十日線為準，多餘的截掉
    plt.savefig(stock2330.sid + ".jpg", bbox_inches="tight")
    plt.show() # 自動存檔，所以不用顯示
    # time.sleep(10) # 避免短時間大量送出request