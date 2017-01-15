'''
Created on Dec 28, 2016

@summary: Questrade paths/urls for restful calls

@note: As a standard we'll leave off leading "/" as the api server has a suffix "/"
    We'll have to remember to add any suffix "/" whenever we make a path
    
@note: Formation: server_api + version + enum_path + / + enum_path ...
    %s is used where an account or symbol name is required


@copyright: 2016
@author: Chris
@license: 

@bug:

'''

class root:
    token_url = 'https://login.questrade.com/oauth2/token?grant_type=refresh_token&refresh_token='
    version = 'v1/'
    
    
class accounts:
    time = 'time'
    accounts = 'accounts'
    positions = 'accounts/%s/positions'
    balances = 'accounts/%s/balances'
    executions = 'accounts/%s/executions'
    orders = 'accounts/%s/orders'
    activities = 'accounts/%s/activities'
    
    
class markets:
    symbols = 'symbols/%s'
    search = 'symbols/search'
    options = 'symbols/%s/options'
    marktes = 'markets'
    quotes = 'markets/quotes/%s'
    quotes_options = 'markets/quotes/options'
    quotes_strategies = 'markets/quotes/strategies'
    candles = 'markets/candles/%s'
    
    
    
class orders:
    orders = 'accounts/%s/orders'  #POST or DELETE - place/replace
    orders_impact = 'accounts/%s/orders/impact' #POST - no impact - simulates order only
    bracket = 'accounts/%s/orders/bracket' #POST
    bracket_impact = 'accounts/%s/orders/bracket/impact' #POST - no impact - simulates order only
    strategy = 'accounts/%s/strategy' #POST
    strategy_impact = 'accounts/%s/strategy/impact' #POST 
    
    