'''
Created on Dec 28, 2016

@summary: Questrade Enumerations for json field names and other standards


@copyright: 2016
@author: Chris
@license: 

@bug:

'''

''' Token
These are the field names in the token response when refreshing a token
'''
class Token:
    access_token = 'access_token'
    api_server = 'api_server'
    expires_in = 'expires_in'
    refresh_token = 'refresh_token'
    token_type = 'token_type'
    token_file = 'QTtoken.json'
    expires_at = 'expires_at'

''' Limits
These are the rate limits per second/hr for restful calls to the API
'''
class Limits:
    account_calls_persec = 30
    account_calls_perhr = 30000
    market_calls_persec = 20
    market_calls_perhr = 15000
    order_calls_persec = 10
    order_calls_perhr = 500
    
    
class Currency:
    USD = 'USD'
    CAD = 'CAD'


class Exchange:
    TSX = 'TSX'
    TSXV = 'TSXV'
    CNSX = 'CNSX'
    MX = 'MX'
    NASDAQ = 'NASDAQ'
    NYSE = 'NYSE'
    AMEX = 'AMEX'
    ARCA = 'ARCA'
    OPRA = 'OPRA'
    PinkSheets = 'PinkSheets'
    OTCBB = 'OTCBB'

class AccountType:
    Cash = 'Cash'
    Margin = 'Margin'
    TFSA = 'TFSA'
    RRSP = 'RRSP'
    SRRSP = 'SRRSP'
    LRRSP = 'LRRSP'
    LIRA = 'LIRA'
    LIF = 'LIF'
    RIF = 'RIF'
    SRIF = 'SRIF'
    LRIF = 'LRIF'
    RRIF = 'RRIF'
    PRIF = 'PRIF'
    RESP = 'RESP'
    FRESP = 'FRESP'
    
class TickType:
    Up = 'Up'
    Down = 'Down'
    Equal = 'Equal'
    
class OrderStateFilterType:
    All = 'All'
    Open = 'Open'
    Closed = 'Closed'
    

class OrderAction:
    Buy = 'Buy'
    Sell = 'Sell'


class OrderSide:
    Buy = 'Buy'
    Sell = 'Sell'
    Short = 'Short'
    Cov = 'Cov'
    BTO = 'BTO'
    STC = 'STC'
    STO = 'STO'
    BTC = 'BTC'

class OrderType:
    Market = 'Market'
    Limit = 'Limit'
    Stop = 'Stop'
    StopLimit = 'StopLimit'
    TrailStopInPercentage = 'TrailStopInPercentage'
    TrailStopInDollar = 'TrailStopInDollar'
    TrailStopLimitInPercentage = 'TrailStopLimitInPercentage'
    TrailStopLimitInDollar = 'TrailStopLimitInDollar'
    LimitOnOpen = 'LimitOnOpen'
    LimitOnClose = 'LimitOnClose'
    
class OrderTimeInForce:
    Day = 'Day'
    GoodTillCanceled = 'GoodTillCanceled'
    GoodTillExtendedDay = 'GoodTillExtendedDay'
    GoodTillDate = 'GoodTillDate'
    ImmediateorCancel = 'ImmediateOrCancel'
    FillOrKill = 'FillOrKill'
    
class HistoricalDataGranularity:
    OneMinute = 'OneMinute'
    TwoMinutes = 'TwoMinutes'
    ThreeMinutes = 'ThreeMinutes'    
    FourMinutes = 'FourMinutes'
    FiveMinutes = 'FiveMinutes'
    TenMinutes = 'TenMinutes'
    FifteenMinutes = 'FifteenMinutes'
    TwentyMinutes = 'TwentyMinutes'
    HalfHour = 'HalfHour'
    OneHour = 'OneHour'
    TwoHours = 'TwoHours'
    FourHours = 'FourHours'
    OneDay = 'OneDay'
    OneWeek = 'OneWeek'
    OneMonth = 'OneMonth'
    OneYear = 'OneYear'

class OrderState:
    Failed = 'Failed'
    Pending = 'Pending'
    Accepted = 'Accepted'
    Rejected = 'Rejected'
    CancelPending = 'CancelPending'
    Canceled = 'Canceled'
    PartialCanceled = 'PartialCanceled'
    Partial = 'Partial'
    Executed = 'Executed'
    ReplacePending = 'ReplacePending'
    Replaced = 'Replaced'
    Stopped = 'Stopped'
    Suspended = 'Suspended'
    Expired = 'Expired'
    Queued = 'Queued'
    Triggered = 'Triggered'
    Activated = 'Activated'
    PendingRiskReview = 'PendingRiskReview'
    ContingentOrder= 'ContingentOrder'


class OrderClass:
    Primary = 'Primary'
    Limit = 'Limit'
    StopLoss = 'StopLoss'
    
class OptionType:
    Call = 'Call'
    Put = 'Put'
    
class AccountStatus:
    active = 'Active'
    suspended_closed = 'Suspended (Closed)'
    suspended_view = 'Suspended (View Only)'
    liquidate = 'Liquidate Only'
    closed = 'Closed'
    
class ClientAccountType:
    individual = 'Individual'
    joint = 'Joint'
    informal_trust = 'Informal Trust'
    corporation = 'Corporation'
    investment_club = 'Investment Club'
    formal_trust = 'Formal Trust'
    partnership = 'Partnership'
    sole_proprietorship = 'Sole Proprietorship'
    family = 'Family'
    joint_informal_trust = 'Joint and Informal Trust'
    institution = 'Institution'
    