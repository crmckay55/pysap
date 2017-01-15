'''
Created on Jan 2, 2017

@author: Chris
'''
import datetime
import json
import os
import pytz
import requests

import dateutil.parser as dateparse
import logging as log
from src.questrade.enums import dictionary as dict
from src.questrade.enums import enums
from src.questrade.enums import urls


class Token(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor: sets the debug and class name.  First refresh of token is not done because when a value
        is accessed (via method) it will check if refresh is needed.
        '''
        self.__debug = True                # Debug
        self.__name = 'Questrade Token'     # Name of class
        self.__expires_at = None            # setting private expires time to none
        self.__token = None                 # set default token to none
        
        # in order to reduce the number of errors in time sensitive calls, we set an expiry buffer
        # to allow time for processes after token check.  This is important for refresh of classes that may take a little
        # time.  This can be moved to a config file later?
        self.__expiry_buffer = 60           
 
    '''
    Below are the public methods of the class.  
    There aren't any attributes in this class because we have to check each time if the token is still valid
    as each time a call is made the values could have changed.
    ''' 
    def api_server(self):
        if self.__is_token_expired__() == True:
            self.__refresh_token__()
            
        return self.__token[enums.Token.api_server]


    def server_time(self):
        if self.__is_token_expired__() == True:
            self.__refresh_token__()
    
        #set call_url for getting time
        __call_url = self.__token[enums.Token.api_server] + urls.root.version + urls.accounts.time
        
        #get header for call
        __headers = {'Authorization': self.__token[enums.Token.token_type] + " " + self.__token[enums.Token.access_token]}
        
        #make call for time and get response
        __t = requests.get(__call_url, headers = __headers)
        __response = __t.json()
       
        #return the time from json response
        return __response[dict.Time.time]  
    
    
    def call_header(self):
        if self.__is_token_expired__() == True:
            self.__refresh_token__()
        
        return {'Authorization': self.__token[enums.Token.token_type] + " " + self.__token[enums.Token.access_token]}  
        
      
    '''
    Below are all the private methods to this class.
    They are private because each needs to check first if the token is refreshed before returning a value.
    '''
    def __is_token_expired__(self):
        # If no expires at value, force refresh
        if self.__expires_at == None:
            return True
        
        # Return boolean if we are past the expiry time
        else:
            __localtz = pytz.timezone('Canada/Mountain')
            __servertz = pytz.timezone('Canada/Eastern')
            __local_date = __localtz.localize(datetime.datetime.now())
            __local_date = __local_date.astimezone(__servertz)
            return self.__expires_at < __local_date
           
             
    def __refresh_token__(self, debug=False):
        # Try to open the Token JSON file first
        userpath = os.getenv("HOME")
        fullpath = userpath + '/' + enums.Token.token_file
        
        try:
            with open(fullpath) as __f:
                __jsonStr = __f.read()
                self.__token = json.loads(__jsonStr)  
                self.__expires_at = dateparse.parse(self.__token[enums.Token.expires_at])
        
        # If we can't open it, then do something.
        except:
            if self.__debug == True: 
                print('get_token() IOError opening old token')
                print(enums.Token.token_file)
            self.__token = None
            return self.__token

        # Now that we've loaded the Token JSON file, check to see if it is expired.  
        # If not, return a valid token
        if self.__is_token_expired__() == False:
            return self.__token
        
        # If it was expired, then we need to use the refresh key to get a new token.
        else:
            
            if self.__debug == True:
                print('get_token() new token requested or required')
                
            __call_url = urls.root.token_url + self.__token[enums.Token.refresh_token]
            
            __r = requests.get(__call_url)
            self.__token = __r.json()
            
            __my_time = dateparse.parse(self.__server_time__()) + datetime.timedelta(seconds = self.__token[enums.Token.expires_in] - self.__expiry_buffer)            
            self.__token[enums.Token.expires_at] = str(__my_time)
            
            with open(fullpath, 'w') as __outfile:
                json.dump(self.__token, __outfile, indent=4, sort_keys=True, separators=(',', ':'))  
        
            log.warning('get_token() returned new token to ' +  str(__r) + ' - ' + str(self.__token))
            
            return self.__token
    
    
    def __delete_token__(self):
        # delete local json file with token
        os.remove(enums.Token.token_file)
        
        
    def __server_time__(self):
        '''
        For method use only as this bypasses the need to check for expired token.
        '''
        #set call_url for getting time
        __call_url = self.__token[enums.Token.api_server] + urls.root.version + urls.accounts.time
        
        #get header for call
        __headers = {'Authorization': self.__token[enums.Token.token_type] + " " + self.__token[enums.Token.access_token]}
        
        #make call for time and get response
        __t = requests.get(__call_url, headers = __headers)
        __response = __t.json()
       
        #return the time from json response
        return __response[dict.Time.time]  
    
    
   
