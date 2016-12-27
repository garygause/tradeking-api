import oauth2 as oauth
import json
from datetime import date
from dateutil.parser import parse

class TKApiClient(object):

    # https://developers.tradeking.com/documentation/
    api_url = "https://api.tradeking.com/v1"

    market_clock_url = api_url + "/market/clock.json"
    market_quotes_url = api_url + "/market/ext/quotes.json"
    market_news_url = api_url + "/market/news/search.json"
    market_newsitem_url = api_url + "/market/news"
    market_options_url = api_url + "/market/options/search.json"

    accounts_url = api_url + "/accounts.json"
    quotes_url = api_url + "/market/ext/quotes.json"

    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = oauth.Token(access_token, access_secret)
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)
        self.client = oauth.Client(self.consumer, self.token)


    def clock(self):
        resp, content = self.client.request(self.market_clock_url, "GET")
        return content 


    def quote(self, symbol='SPY'):
        resp, content = self.client.request(self.market_quotes_url + "?symbols=" + symbol, "GET")
        j = json.loads(content)
        return j['response']['quotes']['quote']


    def news(self, symbol='SPY', max=3):
        resp, content = self.client.request(self.market_news_url + "?symbols=" + symbol + "&maxhits=" + max, "GET")
        j = json.loads(content)
        return j['response']['articles']


    def newsitem(self, id):
        resp, content = self.client.request(self.market_newsitem_url + "/" + id + ".json", "GET")
        j = json.loads(content)
        return j['response']['article']


    def options(self, symbol='SPY'):
        #url = self.market_options_url + "?symbol=" + symbol + "&query=xyear-eq:2017 AND xmonth-eq:01 AND strikeprice-gt:120&fids=ask,bid,vol"
        url = self.market_options_url + "?symbol=" + symbol + "&query=xyear-eq:2017"
        resp, content = self.client.request(url, "GET")
        j = json.loads(content)
        return j['response']['quotes']['quote']

    
    def holdings(self):
        resp, content = self.client.request(self.accounts_url, "GET")
        j = json.loads(content)
        return j['response']['accounts']['accountsummary']


