def price_unit(price):
    unit = 0
    
    if price >= 2000000:
        unit = 1000
    elif price >= 1000000:
        unit = 500
    elif price >= 500000:
        unit = 100
    elif price >= 100000:
        unit = 50
    elif price >= 10000:
        unit = 10
    elif price >= 1000:
        unit = 5
    elif price >= 100:
        unit = 1
    elif price >= 10:
        unit = 0.1
    elif price >= 1:
        unit = 0.01
    elif price >= 0.1:
        unit = 0.001
    else:
        unit = 0.0001
    
    return unit

def total_price(price, volume):
    return price * volume

def is_higher_than_lowerlimitprice(price, volume):
    if total_price(price, volume) > 5000 :
        return True
    else:
        return False

def order_fee(price, volume):
    return total_price(price, volume) * 0.0005