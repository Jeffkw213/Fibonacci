from flask import Flask, request
from requests_cache import CachedSession
import pandas as pd


url = 'https://api.coingecko.com/api/v3/'
coin = 'bitcoin'
error_500 = ({ "error": "Internal Server Error" }, 500)
sessionData = CachedSession(
        cache_name='cache/data',
        expire_after=300)

app = Flask(__name__)

# Get Bitcoin Data for the past 90 days
# Returns prices[UNIX TimeStamp, Price in USD] 


