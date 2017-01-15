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
        self._debug = False  # DEBUG
        
        self._symbol_id_list = symbolIdList  # pass along the symbol list for use in this class
        
        self.__key = Token.Token()  # get a valid token
        
        # Get quote list 
        self._get_market_quote_()  # get the quote for the symbols passed
        
    
    def refresh_market_quote(self):
        # called when we want a refresh of existing symbol list
        self.quoteList = []  # empty quote list
        
        self.__key = Token.Token()  # get refreshed token
        
        self._get_market_quote_()  # refresh quotes
        
    
    def _get_market_quote_(self):
        
        __csvSymbols = ''  # empty string to hold csv'd list of symbols for params
        __separator = ''  # initialize csv adder to blank for symbol list
        __counter = 0  # counter for params builder - add a comma or not?
        
        # get the call header and url
        __header = self.__key.call_header()
        __call_url = self.__key.api_server() + urls.root.version + (urls.markets.quotes % '')
        
        # created concatenated csv list to pass into params
        for __symbol in self._symbol_id_list:
            if __counter > 0:
                __separator = ','
            __csvSymbols = __csvSymbols + __separator + __symbol
            __counter = __counter + 1
            
        # build params from csv symbol list
        __params = {qtD.Quotes.ids: __csvSymbols}           
    
        # make call for accounts and get response
        __t = requests.get(__call_url, headers=__header, params=__params)
        __response = __t.json()

        # get market calls remaining, and reset time, and log
        unix_timestamp = float(__t.headers[qtD.ResponseHeader.XRateLimitReset])
        __servertz = pytz.timezone('Canada/Eastern')
        (datetime.fromtimestamp(unix_timestamp, __servertz).isoformat())
        
        log.warning('Market Data Limit Remaining:' + str(__t.headers[qtD.ResponseHeader.XRateLimitRemaining]) + 
                    ' resetting at ' + str(datetime.fromtimestamp(unix_timestamp, __servertz).isoformat()))
        
        __time = self.__key.server_time()
        
        # for each quote, add on a retrieve time, and add to quote list
        for __quote in __response[qtD.Quotes.quotes]:
            __quote[qtD.Time.retrieveTime] = __time
            self.quoteList.append(__quote)
        
        
class Symbol(object):
    
    def __init__(self, symbolIdList):
        '''
        symbols can be strings or integers
        '''
        
        self.symbolList = []  # initialize list for holding quotes
        self._debug = False  # DEBUG
        self.__key = Token.Token()  # get a valid token
        self._symbol_id_list = symbolIdList  # pass along the symbol list for use in this class
        
        # Get quote list 
        self.__get_symbol_info__()  # get the quote for the symbols passed
        
        
    def __get_symbol_info__(self):
        
        __csvSymbols = ''  # empty string to hold csv'd list of symbols for params
        __separator = ''  # initialize csv adder to blank for symbol list
        __counter = 0  # counter for params builder - add a comma or not?
        
        # get the call header and url
        __header = self.__key.call_header()
        __call_url = self.__key.api_server() + urls.root.version + (urls.markets.symbols % '')
        
        # created concatenated csv list to pass into params
        for __symbol in self._symbol_id_list:
            if __counter > 0:
                __separator = ','
            __csvSymbols = __csvSymbols + __separator + __symbol
            __counter = __counter + 1
            
        # build params from csv symbol list
        if type(self._symbol_id_list[0]) == int:
            __params = {qtD.Symbols.ids: __csvSymbols}  
            print('integer passed')
        if type(self._symbol_id_list[0]) == str:
            __params = {qtD.Symbols.names: __csvSymbols}           
            print('string passed')
            
        # make call for accounts and get response
        __t = requests.get(__call_url, headers=__header, params=__params)
        __response = __t.json()
        
        # get market calls remaining, and reset time, and log
        unix_timestamp = float(__t.headers[qtD.ResponseHeader.XRateLimitReset])
        __servertz = pytz.timezone('Canada/Eastern')
        (datetime.fromtimestamp(unix_timestamp, __servertz).isoformat())
        
        log.warning('Account Limit Remaining:' + str(__t.headers[qtD.ResponseHeader.XRateLimitRemaining]) + 
                    ' resetting at ' + str(datetime.fromtimestamp(unix_timestamp, __servertz).isoformat()))
        
        __time = self.__key.server_time()
        
        # for each quote, add on a retrieve time, and add to quote list
        for __symbol in __response[qtD.Symbols.symbols]:
            __symbol[qtD.Time.retrieveTime] = __time
            self.symbolList.append(__symbol)
