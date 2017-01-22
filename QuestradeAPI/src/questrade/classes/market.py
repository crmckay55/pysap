'''
Created on Jan 8, 2017

@author: Chris
'''
# common imports
from datetime import datetime
import pytz
import requests

import logging as log
import src.questrade.classes.token as Token
import src.questrade.enums.dictionary as qtD
import src.questrade.enums.urls as urls


# questrade imports
class Quotes(object):
    '''
    classdocs
    '''
    def __init__(self, symbolIdList):
        '''
        Constructor
        '''
        self.quoteList = []  # initialize list for holding quotes
        self._debug_ = False  # DEBUG
        
        self._symbol_id_list_ = symbolIdList  # pass along the symbol list for use in this class
        
        self.__key__ = Token.Token()  # get a valid token
        
        # Get quote list 
        self._get_market_quote_()  # get the quote for the symbols passed
        
    
    def refresh_market_quote(self):
        # called when we want a refresh of existing symbol list
        self.quoteList = []  # empty quote list
        
        self.__key__ = Token.Token()  # get refreshed token
        
        self._get_market_quote_()  # refresh quotes
        
    
    def _get_market_quote_(self):
        
        csvSymbols = ''  # empty string to hold csv'd list of symbols for params
        separator = ''  # initialize csv adder to blank for symbol list
        counter = 0  # counter for params builder - add a comma or not?
        
        # get the call header and url
        header = self.__key__.call_header()
        call_url = self.__key__.api_server() + urls.root.version + (urls.markets.quotes % '')
        
        # created concatenated csv list to pass into params
        for symbol in self._symbol_id_list_:
            if counter > 0:
                separator = ','
            csvSymbols = csvSymbols + separator + symbol
            counter = counter + 1
            
        # build params from csv symbol list
        params = {qtD.Quotes.ids: csvSymbols}           
    
        # make call for accounts and get response
        t = requests.get(call_url, headers=header, params=params)
        response = t.json()

        # get market calls remaining, and reset time, and log
        unix_timestamp = float(t.headers[qtD.ResponseHeader.XRateLimitReset])
        servertz = pytz.timezone('Canada/Eastern')
        (datetime.fromtimestamp(unix_timestamp, servertz).isoformat())
        
        log.warning('Market Data Limit Remaining:' + str(t.headers[qtD.ResponseHeader.XRateLimitRemaining]) + 
                    ' resetting at ' + str(datetime.fromtimestamp(unix_timestamp, servertz).isoformat()))
        
        time = self.__key__.server_time()
        
        # for each quote, add on a retrieve time, and add to quote list
        for quote in response[qtD.Quotes.quotes]:
            quote[qtD.Time.retrieveTime] = time
            self.quoteList.append(quote)
        
        
class Symbol(object):
    
    def __init__(self, symbolIdList):
        '''
        symbols can be strings or integers
        '''
        
        self.symbolList = []  # initialize list for holding quotes
        self._debug_ = False  # DEBUG
        self.__key__ = Token.Token()  # get a valid token
        self._symbol_id_list_ = symbolIdList  # pass along the symbol list for use in this class
        
        # Get quote list 
        self.__get_symbol_info__()  # get the quote for the symbols passed
        
        
    def __get_symbol_info__(self):
        
        csvSymbols = ''  # empty string to hold csv'd list of symbols for params
        separator = ''  # initialize csv adder to blank for symbol list
        counter = 0  # counter for params builder - add a comma or not?
        
        # get the call header and url
        header = self.__key__.call_header()
        call_url = self.__key__.api_server() + urls.root.version + (urls.markets.symbols % '')
        
        # created concatenated csv list to pass into params
        for symbol in self._symbol_id_list_:
            if counter > 0:
                separator = ','
            csvSymbols = csvSymbols + separator + symbol
            counter = counter + 1
            
        # build params from csv symbol list
        if type(self._symbol_id_list_[0]) == int:
            params = {qtD.Symbols.ids: csvSymbols}  
            print('integer passed')
        if type(self._symbol_id_list_[0]) == str:
            params = {qtD.Symbols.names: csvSymbols}           
            print('string passed')
            
        # make call for accounts and get response
        t = requests.get(call_url, headers=header, params=params)
        response = t.json()
        
        # get market calls remaining, and reset time, and log
        unix_timestamp = float(t.headers[qtD.ResponseHeader.XRateLimitReset])
        servertz = pytz.timezone('Canada/Eastern')
        (datetime.fromtimestamp(unix_timestamp, servertz).isoformat())
        
        log.warning('Account Limit Remaining:' + str(t.headers[qtD.ResponseHeader.XRateLimitRemaining]) + 
                    ' resetting at ' + str(datetime.fromtimestamp(unix_timestamp, servertz).isoformat()))
        
        time = self.__key__.server_time()
        
        # for each quote, add on a retrieve time, and add to quote list
        for symbol in response[qtD.Symbols.symbols]:
            symbol[qtD.Time.retrieveTime] = time
            self.symbolList.append(symbol)
