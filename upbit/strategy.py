"""
1.단기
 1) Short Golden Cross(SGC) : 5분봉 골든크로스 매수/데드크로스 매도전략
 2) 1시간 변동성 돌파 전략
 3) 1% 초단타 전략

 parameter :
 1. period
 2. 
"""

"""
2. 중장기 전략
 1) Long Golden Cross(LGC) : 일봉 골든크로스 매수/데드크로스 매도전략
 2) 변동성 돌파 전략
 3) 10% 중단기 전략
"""
import pandas as pd

class Strategy:
    def __init__(self):
        pass
    
    def MA(self, data: pd.DataFrame, interval: int=5) -> pd.Series:
        return data.rolling(interval).mean()

    def Bollinger(self, data: pd.DataFrame) -> pd.DataFrame:
        bollinger_upper = data.rolling(20).mean() + data.rolling(20).std() * 2
        bollinger_lower = data.rolling(20).mean() - data.rolling(20).std() * 2
        ma20 = self.MA(data, interval=20)
        
    def SGC(self):
        pass