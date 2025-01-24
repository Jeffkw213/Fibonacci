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




def plot(df):
    df.plot(kind= 'scatter', x='Date', y ='Price')
    plt.show()
    
    
def fibonacci(df) -> None:
    """
    Determines the likeliness of buying and selling base on the fibonacci numbers
    
    Fibonacci retracement is the level on a price chart where the price trajectory is expected to a pullback or stall in its trend.
    
    UR = High price - ((High price - Low price) * percentage) in an uptrend market; or

    UR = Low price + ((High price - Low price) * percentage) in a downtrend market
    
    Percentage: (38.2%, 50%, 61.8%, and 100%) used.
    
    Args:
        df (pd.DataFrame): a table [date, price]

    Returns: the fibonacci ranges (38.2%, 50%) and (50%, 61.8%)
        
    """
    absMin = df["Price"].min()
    absMax = df["Price"].max()
    range = [absMin, absMax]
    _fifty = (absMin + absMax)*.5
    
    
    
    return True



response = sessionData.get(url+"coins/"+str(coin)+"/market_chart", params= params)
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data['prices'])
    df.columns = ['Date', 'Price']
    df['Date'] = pd.to_datetime(df['Date'],unit='ms')
    
    print(df['Price'].min())
    print(df['Price'].max())
    plot(df)
    # fibonacci(df)
    
    
else:
    print(error_500)
    
