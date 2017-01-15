'''
Created on Jan 2, 2017

@summary: Contains all classes of data that can be returned from Questrade of type "Account"
          Positions, Balances, Executions, Orders and Activities.
          Separate sub-class of Account() 

@author: Chris
'''

import requests

import src.questrade.classes.token as Token
import src.questrade.enums.dictionary as qtD
import src.questrade.enums.urls as urls


class AccountList():
    
    
    def __init__(self):
        # set all attribute lists up (null)
        self.status = []
        self.isBilling = []
        self.number = []
        self.isPrimary = []
        self.type = []
        self.clientAccountType = []
        self.name = []
        
        # Get new token
        self.__key = Token.Token()
        self.__debug = False
        
        # Get Account list as a JSON response from Questrade
        __jsonResponse = self.__get_account_info__()
        
        # Set the class lists from JSON response
        self.__set_account_lists__(__jsonResponse)
        
        # PUBLIC Questrade userId
        self.userId = __jsonResponse[qtD.Accounts.userid]
        
        # PUBLIC quantity of accounts to help with iterations over data              
        self.accountQty = len(__jsonResponse[qtD.Accounts.accounts])    
    
    
    def __get_account_info__(self):
        # set call url and header based on key and account url buildup from enums
        __call_url = self.__key.api_server() + urls.root.version + urls.accounts.accounts
        __header = self.__key.call_header()
         
        # make call for accounts and get response
        __t = requests.get(__call_url, headers=__header)
        __response = __t.json()
    
        # DEBUG
        if self.__debug == True:
            print('get_accounts() call_url: ' + str(__call_url))
            print('get_accounts() headers: ' + str(__header))
            print('get_account() json response header: ' + str(__t))
            print('get_accounts() json response: ' + str(__response))
            print('')
       
        return __response
    
    
    def refreshAccounts(self):
        # refresh accounts by calling the __init__ again, which will also get fresh token if needed
        self.__init__()
    
    
    def __set_account_lists__(self, __jsonResponse):
        
        # iterate through each account in JSON response and add to list of attributes
        for __entry in __jsonResponse[qtD.Accounts.accounts]:
            self.status.append(__entry[qtD.Accounts.status])
            self.isBilling.append(__entry[qtD.Accounts.isbilling])
            self.number.append(__entry[qtD.Accounts.number])
            self.isPrimary.append(__entry[qtD.Accounts.isprimary])
            self.type.append(__entry[qtD.Accounts.type])
            self.clientAccountType.append(__entry[qtD.Accounts.client_account_type])
            self.name.append(__entry[qtD.Accounts.number])


class AccountBalances():
    
    def __init__(self, acctId):
        self.name = acctId
        
        self.perCurrencyBalances = []
        self.combinedBalances = []
        self.sodPerCurrencyBalances = []
        self.sodCombinedBalances = []

        self.__key = Token.Token()  
        self.__debug = False
        
        self.__get_balances__()
        
        
    def __get_balances__(self):
        
        __header = self.__key.call_header()
        __call_url = self.__key.api_server() + urls.root.version + (urls.accounts.balances % self.name)
    
        # make call for accounts and get response
        __t = requests.get(__call_url, headers=__header)
        __response = __t.json()
        
        if self.__debug == True:
            print(str(__response))
        
        for __entry in __response[qtD.Balances.perCurrencyBalances]:
            self.perCurrencyBalances.append(__entry)
            
        for __entry in __response[qtD.Balances.combinedBalances]:
            self.combinedBalances.append(__entry)  
        
        for __entry in __response[qtD.Balances.sodPerCurrencyBalances]:
            self.sodPerCurrencyBalances.append(__entry) 
            
        for __entry in __response[qtD.Balances.sodCombinedBalances]:
            self.sodCombinedBalances.append(__entry)
   
            
            
            
# class Executions(List):

# class Orders(List):
    
# class Activities(List):

    
   
        


