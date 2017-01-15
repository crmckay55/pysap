'''
Created on Jan 2, 2017

@author: Chris
'''

from Tkinter import *
from ttk import Treeview


import logging as log
from src.questrade.classes import market
import src.questrade.classes.account as Account
from src.questrade.classes.token import Token
from src.questrade.enums import dictionary as qtD


log.basicConfig(filename=('test.log'), format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
log.warning('----------Start of CLASSTEST')

symbolIdList = []

symbols =['AGU.TO','MX.TO','IT.TO']
print(symbols)
symbolInfo = market.Symbol(symbols)
for __symbol in symbolInfo.symbolList:
    print(str(__symbol))
    symbolIdList.append(str(__symbol[qtD.Symbols.symbolId]))
    
print('')
print(str(symbolIdList))
print('')
quotes = market.Quotes(symbolIdList)
for __quote in quotes.quoteList:
    print(str(__quote[qtD.Quotes.symbol]) + ' last trade price: ' + str(__quote[qtD.Quotes.lastTradePrice]))
    



key = Token()
print(key.call_header())
print(key.api_server())
print(key.server_time())


acct = Account.AccountList()
print(acct.userId)

balances =[]


for i in range(acct.accountQty):
    index = (i)
    balances.append(Account.AccountBalances(acct.name[index]))
    print('index',index)
    print('type', acct.type[index])
    print('account', acct.number[index])
    print('name', acct.name[index])
    print('')

'''
for i in range(acct.accountQty):
    print(acct.name[i])
    print(acct.type[i])
       
    for z in range(acct.accountQty):
        print(
                qtD.Balances.perCurrencyBalances + ": " +
                str(balances[i].perCurrencyBalances[z][qtD.Balances.currency]) + ": " + 
                str(balances[i].perCurrencyBalances[z])
             )
        print(
                qtD.Balances.sodCombinedBalances + ": " +
                str(balances[i].sodCombinedBalances[z][qtD.Balances.currency]) + ": " + 
                str(balances[i].sodCombinedBalances[z])
            )
         
        print(
                qtD.Balances.combinedBalances + ": " +
                str(balances[i].combinedBalances[z][qtD.Balances.currency]) + ": " + 
                str(balances[i].combinedBalances[z])
            )
        
        print(
                qtD.Balances.sodPerCurrencyBalances + ": " +
                str(balances[i].sodPerCurrencyBalances[z][qtD.Balances.currency]) + ": " + 
                str(balances[i].sodPerCurrencyBalances[z])
            )
        
    print('')
''' 

root = Tk()


def OnDoubleClick(event):
    item = tree.selection()[0]
    statuslabel.config(text="you clicked on " + tree.item(item,"text"))

tree = Treeview(root)
root.wm_state('zoomed')

print(root.maxsize())


    
# Inserted at the root, program chooses id:
tree["columns"] = ("CAD","USD")
tree.column("CAD", width=100)
tree.heading("CAD", text="CAD")
tree.column("CAD", anchor="e")
   
tree.column("USD", width = 100)
tree.heading("USD",text="USD")
tree.column("USD", anchor="e")   

for i in range(acct.accountQty):
    index = (i) 
    tree.insert('', 'end', acct.type[index],text=acct.type[index], 
                values=('$' + '{:7,.2f}'.format(balances[index].combinedBalances[0]['cash']),
                        '$' + '{:7,.2f}'.format(balances[index].combinedBalances[1]['cash'])
                        )
                )
    
    tree.insert(acct.type[index], 'end', acct.number[index], text = 'Acct Number: ' + acct.number[index])

tree.bind("<ButtonRelease-1>", OnDoubleClick)

tree.pack()


statuslabel = Label(root, bd=1, relief=SUNKEN, anchor=W)
statuslabel.config(text='test status bar')
statuslabel.pack(fill=X)



root.update()
mainloop()


    

