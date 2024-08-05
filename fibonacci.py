from requests_cache import CachedSession
import pandas as pd
from typing import List

import matplotlib.pyplot as plt
import plotly.graph_objects as go 



url = 'https://api.coingecko.com/api/v3/'
coin = 'bitcoin'
params = {
    'vs_currency': 'USD',
    'days': 30
}

error_500 = ({ "error": "Internal Server Error" }, 500)
sessionData = CachedSession(
        cache_name='cache/data',
        expire_after=300)


    


Vector = List[float]



def plot(df):
    df.plot(kind= 'scatter', x='Date', y ='Price')
    plt.show()
    
def plotOHLC(df):
    fig = go.Figure(data=go.Ohlc(
                x=df['Date'],
                open= df['open'],
                high= df['high'],
                low= df['low'],
                close = df['close']
            ))
    fig.show()
    
def fibonacci(df) -> Vector:
    """
    Determines the likeliness of buying and selling base on the fibinocci numbers
    Fibonacci ratios (23.6%, 38.2%, 50%, 61.8%, and 100%) used.
    
    uptrend and downtrends
    
    Args:
        df (pd.DataFrame): a table [date, price]

    Returns:
        [float, float]: the likeliness of buying and likeliness of selling 
    """
    
    
    
    
    return [0,0]



# response = sessionData.get(url+"coins/"+str(coin)+"/market_chart", params= params)
# if response.status_code == 200:
#     data = response.json()
#     df = pd.DataFrame(data['prices'])
#     df.columns = ['Date', 'Price']
#     df['Date'] = pd.to_datetime(df['Date'],unit='ms')
    
    
#     plot(df)
#     # fibonacci(df)
    
    
# else:
#     print(error_500)
    

getOHLC = sessionData.get(url+"coins/"+str(coin)+"/ohlc", params= params)
if getOHLC.status_code == 200:
    data = getOHLC.json()
    df = pd.DataFrame(data)
    df.columns = ['Date','open','high', 'low', 'close']
    df['Date'] = pd.to_datetime(df['Date'],unit='ms')
    plotOHLC(df)
    print(df)
else:
    print(error_500)