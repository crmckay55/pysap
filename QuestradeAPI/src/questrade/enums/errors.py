'''
Created on Dec 28, 2016

@author: Chris
'''

# HTTPstatuscode HTTPstatusmessage    Error code    Error message
#  404        Not Found                 1001    Invalid endpoint.
#  400        Bad Request               1002    Invalid or malformed argument.
#  400        Bad Request               1003    Argument length exceeds imposed limit.
#  400        Bad Request               1004    Missing required argument.
#  413        Request Entity Too Large  1005    Request length exceeds imposed limit.
#  429        Too Many Requests         1006    Rate limit exceeded.
#  500        Internal Server Error     1007    IQ servers responded with a business error.
#  500        Internal Server Error     1008    IQ servers responded with a technical error.
#  500        Internal Server Error     1009    IQ servers responded with an unexpected error.
#  502        Bad Gateway               1010    IQ servers produced an invalid response.
#  503        Gateway Timeout           1011    IQ servers did not produce a response before a timeout.
#  405        Method Not Allowed        1012    Method unsupported by endpoint (e.g., GET vs. POST).
#  400        Bad Request               1013    Requesting anything other than ‘application/json’.
#  401        Unauthorized              1014    Missing authorization header.
#  400        Bad Request               1015    Malformed authorization header.
#  403        Forbidden                 1016    Request is out-of-allowed OAuth scopes.
#  401        Unauthorized              1017    Access token is invalid.
#  404        Not Found                 1018    Account number not found.
#  404        Not Found                 1019    Symbol not found.
#  404        Not Found                 1020    Order not found.
#  500        Internal Server Error     1021    Unexpected error (with undefined handling).


class HTTPstatuscode:
    NotFound = '404'
    BadRequest = '400'
    ReqestEntityTooLarge = '413'
    TooManyRequestss = '429'
    InternalServerError = '500'
    BadGateway = '502'
    GatewayTimeout = '503'
    MethodNotAllowed = '405'
    Unauthorized = '401'
    Forbidden = '403'
    
class ErrorCode:
    InvalidEndpoint = '1001'
    InvalidArgument = '1002'
    ArgExceedsLengthLimit = '1003'
    MissingRequiredArg = '1004'
    RequestExceedsLengthLimit = '1005'
    RateLimitExceeded = '1006'
    IQServerBusinessError = '1007'
    IQServerTechnicalError = '1008'
    IQServerUnexpectedError = '1009'
    IQServerInvalidResponse = '1010'
    IQServerTimeout = '1011'
    MethodUnsupported = '1012'
    ReqOtherThanJson = '1013'
    MissingAuthHeader = '1014'
    MalformedAuthHeader = '1015'
    ReqOutOfOAuthScopes = '1016'
    AccessTokenInvalid = '1017'
    AccountNumberNotFound = '1018'
    SymbolNotFound = '1019'
    OrderNotFound = '1020'
    UnexpectedError = '1021'
    
    
    
    