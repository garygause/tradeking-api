import oauth2 as oauth
import json
from datetime import date
from dateutil.parser import parse

class TKApiClient(object):

    # https://developers.tradeking.com/documentation/
    API_URL = "https://api.tradeking.com/v1"
    STREAM_URL = "https://stream.tradeking.com/v1"

    market_clock_url = api_url + "/market/clock.{0}"
    market_quotes_url = api_url + "/market/ext/quotes.{0}"
    market_news_url = api_url + "/market/news/search.{0}"
    market_newsitem_url = api_url + "/market/news"
    market_options_url = api_url + "/market/options/search.{0}"

    accounts_url = api_url + "/accounts."
    quotes_url = api_url + "/market/ext/quotes."

    def __init__(self, access_token, access_secret, consumer_key, consumer_secret):
        self.access_token = access_token
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.token = oauth.Token(access_token, access_secret)
        self.consumer = oauth.Consumer(consumer_key, consumer_secret)
        self.client = oauth.Client(self.consumer, self.token)
        self.rtype = 'json'

#    def response_type(self):
#        return self.rtype

    def response_type(self, rtype):
        self.rtype = rtype

    def accounts(self):
        url = '{0}/accounts.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def accounts_balances(self):
        url = '{0}/accounts/balances.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def accounts_id(self, id):
        url = '{0}/accounts/{1}.{2}'.format(self.API_URL, id, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def accounts_id_balances(self, id):
        url = '{0}/accounts/{1}/balances.{2}'.format(self.API_URL, id, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def accounts_id_history(self, id, range='all', transactions='all'):
        """
        param id: id of the account
        param range: all, today, current_week, current_month, last_month
        param transactions: all, bookkeeping, trade
        """
        payload = urllib.urlencode(dict(range=range, transactions=transactions))
        url = '{0}/accounts/{1}/history.{2}?{3}'.format(self.API_URL, id, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def accounts_id_holdings(self, id):
        url = '{0}/accounts/{1}/holdings.{2}'.format(self.API_URL, id, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def accounts_id_orders(self, id):
        url = '{0}/accounts/{1}/orders.{2}'.format(self.API_URL, id, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def accounts_id_orders(self, id, method='GET', fixml=None, headers=None):
        url = '{0}/accounts/{1}/orders.{2}'.format(self.API_URL, id, self.format)
        if method.lower() == 'get':
            response, content = self.oAuthRequest.request(url)
            return content, response
        elif method.lower() == 'post':
            response, content = self.oAuthRequest.request(url, body=fixml, headers=headers, method=method)
            return content, response, fixml, headers
        else:
            raise "Invalid method {}".format(method)

    def accounts_id_orders_preview(self, id, fixml):
        url = '{0}/accounts/{1}/orders/preview.{2}'.format(self.API_URL, id, self.format)
        response, content = self.oAuthRequest.request(url, body=fixml, method='POST')
        return content, response, fixml

    def market_clock(self):
        url = '{0}/market/clock.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content) 
        return content

    def market_ext_quotes(self, symbols, fids=''):
        payload = urllib.urlencode(dict(symbols=symbols, fids=fids))
        url = '{0}/market/ext/quotes.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def market_historical_search(self, symbols, interval, startdate, enddate):
        payload = urllib.urlencode(dict(symbols   = symbols, 
                                        interval  = interval,
                                        startdate = startdate,
                                        enddate   = enddate))
        url = '{0}/market/historical/search.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def market_news_search(self, keywords, startdate, enddate, symbols=None, maxhits=10):
        payload = urllib.urlencode(dict(keywords  = keywords, 
                       symbols   = symbols, 
                       maxhits   = maxhits,
                       startdate = startdate, 
                       enddate   = enddate))
        url = '{0}/market/news/search.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_news_id(self, id):
        url = '{0}/market/news/{1}.{2}'.format(self.API_URL, id, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_options_search(self, symbol, query=None, fids=None):
        payload = urllib.urlencode(dict(symbol=symbol, query=query, fids=fids))
        url = '{0}/market/options/search.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_options_strikes(self, symbol):
        payload = urllib.urlencode(dict(symbol=symbol))
        url = '{0}/market/options/strikes.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_options_expirations(self, symbol):
        payload = urllib.urlencode(dict(symbol=symbol))
        url = '{0}/market/options/expirations.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_timesales(self, symbol):
        payload = urllib.urlencode(dict(symbol=symbol))
        url = '{0}/market/options/expirations.{1}?{2}'.format(self.API_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def market_toplists(self, toplist, exchange='N'):
        """
        Exchange abbreviations: (the default exchange is NYSE)
        A:  American Stock Exchange
        N:  New York Stock Exchange
        Q:  NASDAQ
        U:  NASDAQ Bulletin Board
        V:  NASDAQ OTC Other

        Available list types include:
        toplosers       Top losers by dollar amount
        toppctlosers    Top percentage losers
        topvolume       Top volume
        topactive       Top active
        topgainers      Top gainers by dollar amount
        toppctgainers   Top percentage gainers
        """
        payload = urllib.urlencode(dict(exchange=exchange))
        url = '{0}/market/toplists/{1}.{2}?{3}'.format(self.API_URL, toplist, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def member_profile(self):
        url = '{0}/member/profile.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def utility_status(self):
        url = '{0}/utility/status.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def utility_version(self):
        url = '{0}/utility/version.{1}'.format(self.API_URL, self.rtype)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content

    def watchlists(self, name=None, symbols=None, method='GET'):
        if method.lower() == 'post':
            if name is None:
                raise "Need name for watchlist"
            elif symbols is None:
                raise "Need symbols to POST"
            else:
                payload = urllib.urlencode(dict(symbols=symbols, id=name))
                url = '{0}/watchlists.{1}?{2}'.format(self.API_URL, self.rtype, payload)
                resp, content = self.client.request(url, "GET")
                if (self.rtype == 'json'):
                    return json.loads(content)
                return content
        elif method.lower() == 'get':
            url = '{0}/watchlists.{1}'.format(self.API_URL, self.rtype)
            resp, content = self.client.request(url, "GET")
            if (self.rtype == 'json'):
                return json.loads(content)
            return content
        else:
            raise 'Invalid method {}'.format(method)

    def watchlists_id(self, name, method='GET'):
        url = '{0}/watchlists/{1}.{2}'.format(self.API_URL, name, self.rtype)
        if method.lower() == 'get':
            resp, content = self.client.request(url, "GET")
            if (self.rtype == 'json'):
                return json.loads(content)
            return content
        elif method.lower() == 'delete':
            return self.client.delete(url)
        else:
            raise 'Invalid method {}'.format(method)

    def watchlists_id_symbols(self, name, symbols, method='POST'):
        """
        [POST] - add the symbols in the form parameters to the watchlist
                 specified in the URI

        [DELETE] - delete the symbol in the URI for the watchlist specified in
                   the URI
        """
        url = '{0}/watchlists/{1}/symbols.{2}'.format(self.API_URL, name, self.rtype)
        if method.lower() == 'post':
            resp, content = self.client.request(url)
            if (self.rtype == 'json'):
                return json.loads(content)
            return content
        elif method.lower() == 'delete':
            return self.client.delete(url)
        else:
            raise 'Invalid method {}'.format(method)


    def market_quotes(self, symbols):
        payload = urllib.urlencode(dict(symbols=symbols))
        url = '{0}/market/quotes.{1}?{2}'.format(self.STREAM_URL, self.rtype, payload)
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content













    def news(self, symbol='SPY', max=3):
        url = self.market_news_url.format(self.rtype)
        resp, content = self.client.request(url + "?symbols=" + symbol + "&maxhits=" + max, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def newsitem(self, id):
        url = self.market_newsitem_url + "/" + id + "." + self.rtype
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content


    def options(self, symbol='SPY'):
        #url = self.market_options_url + "?symbol=" + symbol + "&query=xyear-eq:2017 AND xmonth-eq:01 AND strikeprice-gt:120&fids=ask,bid,vol"
        url = self.market_options_url.format(self.rtype) + "?symbol=" + symbol + "&query=xyear-eq:2017"
        resp, content = self.client.request(url, "GET")
        if (self.rtype == 'json'):
            return json.loads(content)
        return content
   
 
    def holdings(self):
        resp, content = self.client.request(self.accounts_url, "GET")
        if (self.format == 'json'):
            return json.loads(content)
        return content

