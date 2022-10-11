
"""
parameter :
 1. order_period: 거래주기(1시간, 1일, 1주)
 2. period: ohlcv 주기(minute1,3,5,10,15,30,60,120,240)

1.단기
 1) Short Golden Cross(SGC) : 5분봉 골든크로스 매수/데드크로스 매도전략
 2) 1시간 변동성 돌파 전략
 3) 1% 초단타 전략

 parameter :
 1. order_period: 거래주기(1시간)
 2. period: ohlcv 주기(minute1,3,5,10,15)

2. 중기 전략
 1) Long Golden Cross(LGC) : 1시간봉 골든크로스 매수/데드크로스 매도전략
 2) 변동성 돌파 전략
 3) 10% 중단기 전략

3. 장기 전략
 1) LGC : 
"""
import numpy as np
import pandas as pd
import pyupbit

class Strategy:
    def __init__(self, ticker: str, interval: str, count: int) -> None:
        self.interval = int(interval[6:])
        self.ohlcv = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=count)
        # Linear Interpolation으로 결측치 채우기
        self.ohlcv = self.ohlcv.interpolate(method='linear', limit_direction='forward')
        self.data = self.ohlcv.close
    
    def MA(self, interval: int=5) -> pd.Series:
        return self.data.rolling(interval).mean()

    def WMA(self, interval: int=5) -> pd.Series:
        weights = np.arange(1, 1 + interval)
        return self.data.rolling(interval).apply(lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)

    def Bollinger(self) -> pd.DataFrame:
        bollinger_upper = self.MA(self.data, interval=20) + self.data.rolling(20).std() * 2
        bollinger_lower = self.MA(self.data, interval=20) - self.data.rolling(20).std() * 2
        ma20 = self.MA(self.data, interval=20)
        return pd.concat([bollinger_lower, ma20, bollinger_upper],
                         columns=['lower', 'mean', 'upper'])



class Short_Strategy(Strategy):
    def __init__(self, ticker="KRW-BTC", interval="minute15", count=200) -> None:
        super().__init__(ticker, interval, count)
    
    def SGC(self):
        """
        Short Golden Cross: 매수시점 기준
        """
        check1 = self.MA(60).iloc[-1 - (60 / self.interval)] - self.MA(5).iloc[-1 - (60 / self.interval)] > 0
        check2 = self.MA(60)[-1] - self.MA(5)[-1] < 0
        return check1 & check2

    def SDC(self):
        """
        Short Dead Cross: 매도시점 기준
        """
        check1 = self.MA(60).iloc[-1 - (60 / self.interval)] - self.MA(5).iloc[-1 - (60 / self.interval)] < 0
        check2 = self.MA(60)[-1] - self.MA(5)[-1] > 0
        return check1 & check2
