import pyupbit
from prophet import Prophet

def predict_price(ticker="KRW-BTC", interval = "minute60", count = 200, periods = 24, freq = 'H'):
    df = pyupbit.get_ohlcv(ticker=ticker, interval=interval, count=count)
    df = df.reset_index()
    df['ds'] = df['index']
    df['y'] = df['close']
    data = df[['ds','y']]

    model = Prophet()
    model.fit(data)
    future = model.make_future_dataframe(periods=periods, freq=freq)
    forecast = model.predict(future)
    return forecast[['trend', 'trend_lower','trend_upper']].iloc(-1)