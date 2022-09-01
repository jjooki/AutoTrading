import numpy as np
import pandas as pd
import os
import order

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

def is_higher_than_lower_limit(price, volume):
    if total_price(price, volume) > 5000 :
        return True
    else:
        return False

def order_fee(price, volume, exchange = "upbit", leverage = 1):
    if exchange == "upbit":
        return total_price(price, volume) * 0.0005
    elif exchange == "binance":
        return total_price(price, volume) * leverage * 0.001

def trading_fee(ticker, volume, from_="upbit", to_="binance"):
    if from_ == "upbit":
        df = pd.read_csv('./withdraw_fee.csv')

if __name__ == "__main__":
    # os.path.abspath(os.path.realpath(__file__))
    path_ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
    # print(path_)
    print(mrq.market_info('KRW-XRP'))
    
    # df = pd.read_csv(path_ + '/withdraw_fee.csv', sep=',')
    # print(df)
    # fee_dict = {}
    # for ticker in df.columns:
    #     if ticker == '구분' or ticker == 'KRW':
    #         continue
    #     print(ticker)
    #     price = mrq.trade_price(ticker)
    #     fee_dict[ticker] = df.loc[0,ticker] * price
    #     print(f"{ticker}의 현재 가격은 {price}입니다.")


