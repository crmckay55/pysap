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
        #=======================================================================
        # # set all attribute lists up and get token
        #=======================================================================
        self.status = []                # enums.AccountStatus
        self.isBilling = []             # bool
        self.number = []                # account number
        self.isPrimary = []             # bool
        self.type = []                  # enums.AccountType
        self.clientAccountType = []     # TODO: what is this?
        
        
        self._debug_ = True             # debug TODO: make gloal debug
        
        # Get new token
        self.__key__ = Token.Token()      # local copy of token

        #=======================================================================
        # now that we have the token, get/set all account info
        #=======================================================================
        # Get Account list as a JSON response from Questrade
        jsonResponse = self.__get_account_info__()
        
        if self._debug_ == True:
            print(str(jsonResponse))
        
        # Set the class lists from JSON response
        self.__set_account_lists__(jsonResponse)
        
        # PUBLIC Questrade userId
        self.userId = jsonResponse[qtD.Accounts.userid]
        
        # PUBLIC quantity of accounts to help with iterations over data              
        self.accountQty = len(jsonResponse[qtD.Accounts.accounts])    
    
    def refreshAccounts(self):
        # refresh accounts by calling the __init__ again, which will also get fresh token if needed
        self.__init__()
   
   
    def __get_account_info__(self):
        # set call url and header based on key and account url buildup from enums
        call_url = self.__key__.api_server() + urls.root.version + urls.accounts.accounts
        header = self.__key__.call_header()
         
        # make call for accounts and get response
        t = requests.get(call_url, headers=header)
        response = t.json()
    
        # DEBUG
        if self._debug_ == True:
            print('get_accounts() call_url: ' + str(call_url))
            print('get_accounts() headers: ' + str(header))
            print('get_account() json response header: ' + str(t))
            print('get_accounts() json response: ' + str(response))
            print('')
       
        return response
    
    
    def __set_account_lists__(self, jsonResponse):
        
        # iterate through each account in JSON response and add to list of attributes
        for entry in jsonResponse[qtD.Accounts.accounts]:
            self.status.append(entry[qtD.Accounts.status])
            self.isBilling.append(entry[qtD.Accounts.isbilling])
            self.number.append(entry[qtD.Accounts.number])
            self.isPrimary.append(entry[qtD.Accounts.isprimary])
            self.type.append(entry[qtD.Accounts.type])
            self.clientAccountType.append(entry[qtD.Accounts.client_account_type])


class AccountBalances():
    
    def __init__(self, acctId):
        self.name = acctId
        
        # each of these public items are a list as there are two currencies in each
        self.perCurrencyBalances = []
        self.combinedBalances = []
        self.sodPerCurrencyBalances = []
        self.sodCombinedBalances = []

        self.__key__ = Token.Token()  
        self._debug_ = True
        
        self.__get_balances__()
        
        
    def __get_balances__(self):
        
        header = self.__key__.call_header()
        call_url = (
                    self.__key__.api_server() +             #api server name
                    urls.root.version +                     #version
                    (urls.accounts.balances % self.name)    #account balance url, with name of instance as account ID
                    ) 
    
        # make call for accounts and get response
        t = requests.get(call_url, headers=header)
        response = t.json()
        
        if self._debug_ == True:
            print(str(response))
        
        for entry in response[qtD.Balances.perCurrencyBalances]:
            self.perCurrencyBalances.append(entry)
            
        for entry in response[qtD.Balances.combinedBalances]:
            self.combinedBalances.append(entry)  
        
        for entry in response[qtD.Balances.sodPerCurrencyBalances]:
            self.sodPerCurrencyBalances.append(entry) 
            
        for entry in response[qtD.Balances.sodCombinedBalances]:
            self.sodCombinedBalances.append(entry)
   
            
            
# class Executions(List):

# class Orders(List):
    
# class Activities(List):

    
   
        


