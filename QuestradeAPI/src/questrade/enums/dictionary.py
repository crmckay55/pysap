'''
Created on Dec 30, 2016

@author: Chris
'''

class ResponseHeader:
    XRateLimitRemaining = 'X-RateLimit-Remaining'
    XRateLimitReset = 'X-RateLimit-Reset'
    
class Time:
    time = 'time'                               #time
    retrieveTime = 'retrieveTime'
    
class Accounts:
    userid = 'userId'
    accounts = 'accounts'                       #str
    type = 'type'                               #str - enums.AccountType
    number = 'number'                           #str
    status = 'status'                           #str - enums.AccountStatus
    isprimary = 'isPrimary'                     #bool
    isbilling = 'isBilling'                     #bool
    client_account_type = 'clientAccountType'   #string - enums.ClientAccountType
    
class Positions:
    positions = 'positions'
    symbol = 'symbol'                           #str - symbol ID
    symbolId = 'symbolId'                       #int - Questrade number
    openQuantity = 'OpenQuantity'               #dbl - remaining open
    closedQuantity = 'closedQuantity'           #dbl - portion closed today    
    currentMarketValue = 'currentMarketValue'   #dbl - qty * price
    currentPrice = 'currentPrice'               #dbl
    averageEntryPrice = 'averageEntryPrice'     #dbl
    closedPnL = 'closedPnL'                     #dbl
    totalCost = 'totalCost'                     #dbl 
    isRealTime = 'isRealTime'                   #bool - did real time quote comput PnL?
    isUnderReorg = 'isUnderReorg'               #bool - is symbol currently undergoing reorg
    
class Balances:
    perCurrencyBalances = 'perCurrencyBalances' #json
    combinedBalances = 'combinedBalances'       #json
    sodPerCurrencyBalances = 'sodPerCurrencyBalances'   #json
    sodCombinedBalances = 'sodCombinedBalances' #json
    Balance = 'Balance'                         #json
    currency = 'currency'                       #enum - enums
    cash    =   'cash'                          #dbl - balance amount
    marketValue = 'marketValue'                 #dbl - market value of all securities in account
    totalEquity = 'totalEquity'                 #dbl- difference between cash and marketValue
    buyingPower = 'buyingPower'                 #dbl - buying power for that particular currency side of the account
    maintenanceExcess = 'maintenanceExcess'     #dbl - maint excess for that particular side of account
    isRealTime = 'isRealTime'                   #dbl - was real-time data used to calculate the above values
    

class Activities:
    startTime = 'startTime'                     #DateTime
    endTime = 'endTime'                         #DateTime
    activities = 'activities'
    AccountActivity = 'AccountActivity'         #json
    tradeDate = 'tradeDate'                     #DateTime
    transactionDate = 'transactionDate'         #DateTime
    settlementDate = 'settlementDate'           #DateTime
    action = 'action'                           #str
    symbol = 'symbol'                           #str
    symbolId = 'symbolId'                       #uint64
    description = 'description'                 #str
    currency = 'currency'                       #enum
    quantity = 'quantity'                       #dbl
    price = 'price'                             #dbl
    grossAmount = 'grossAmount'                 #dbl
    commission = 'commission'                   #dbl
    netAmount = 'netAmount'                     #dbl
    type = 'type'                               #str
    maxHistory = 31                             #int
    

class Quotes:
    ids = 'ids'
    quotes = 'quotes'
    symbol = 'symbol'
    symbolId = 'symbolId'
    high52w = 'high52w'
    openPrice = 'openPrice'
    tier = 'tier'
    low52w = 'low52w'
    highPrice = 'highPrice'
    lastTradePrice = 'lastTradePrice'
    VWAP = 'VWAP'                               # volume weighted average price
    delay = 'delay'
    isHalted = 'isHalted'                       #bool
    askPrice = 'askPrice'
    askSize = 'askSize'
    volume = 'volume'
    lastTradeSize = 'lastTradeSize'
    bidSize = 'bidSize'
    lowPrice = 'lowPrice'
    lastTradeTime = 'lastTradeTime'             #datetime
    lastTradePriceTrHrs = 'lastTradePriceTrHrs' #????
    lastTradeTick = 'lastTradeTick'
    bidPrice = 'bidPrice'
    
    
class Symbols:
    ids = 'ids'
    names = 'names'
    symbols = 'symbols'
    symbolId = 'symbolId'
    
    