'''
Created on Jan 2, 2017

@author: Chris
'''

from Tkinter import *
from Tkinter import Frame

from ttk import Treeview
from ttk import Notebook
import os


import logging as log

from src.questrade.classes import market
import src.questrade.classes.account as Account
from src.questrade.classes.token import Token
from src.questrade.enums import dictionary as qtD

userpath = os.getenv("HOME")
fullpath = userpath + '/' + 'test.log'
log.basicConfig(filename=(fullpath), format='%(asctime)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
log.warning('----------Start of CLASSTEST')

symbolIdList = []

symbols =['AGU.TO','MX.TO','IT.TO']
print(symbols)
symbolInfo = market.Symbol(symbols)
for symbol in symbolInfo.symbolList:
    print(str(symbol))
    symbolIdList.append(str(symbol[qtD.Symbols.symbolId]))
    
print('')
print(str(symbolIdList))
print('')
quotes = market.Quotes(symbolIdList)
for quote in quotes.quoteList:
    print(str(quote[qtD.Quotes.symbol]) + ' last trade price: ' + str(quote[qtD.Quotes.lastTradePrice]))
    



key = Token()
print(key.call_header())
print(key.api_server())
print(key.server_time())


acct = Account.AccountList()
print(acct.userId)


balances =[]

for i in range(acct.accountQty):
    index = (i)
    print('index',index)
    print('type', acct.type[index])
    print('account', str(acct.number[index]))
    print('')
    balances.append(Account.AccountBalances(acct.number[index]))



root = Tk()


def OnReleaseClick(event):
    curritem = tree.selection()[0]
    statuslabel.config(text="you clicked on " + tree.item(curritem,"text"))
    try:
        values = tree.item(curritem, "values")[0]
        print(values)
    except:
        print('no values for AcctId')
    


tree = Treeview(root, height = 5)
tree.grid(row=0,column=0)


n = Notebook(root, height=100, width = 300)
n.grid(row=1,column=1)
f1 = Frame(n)   # first page, which would get widgets gridded into it
f2 = Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')
n.grid(row=2)

f1button= Button(f1, text="test", callback=None)
f1button.grid(row=0,column=0)

root.wm_state('zoomed')



print(root.maxsize())


    
# Inserted at the root, program chooses id:
tree["columns"] = ("AcctId","CAD","USD")

tree.column("AcctId", width = 100)
tree.heading("AcctId",text="AcctID")
tree.column("AcctId", anchor="center")  

tree.column("CAD", width=100)
tree.heading("CAD", text="CAD")
tree.column("CAD", anchor="center")
   
tree.column("USD", width = 100)
tree.heading("USD",text="USD")
tree.column("USD", anchor="center")   

for i in range(acct.accountQty):
    index = (i) 
    tree.insert('', 'end', acct.type[index],text=acct.type[index], 
                values=(
                        acct.number[index],
                        '$1,000', #+ '{:7,.2f}'.format(balances[index].combinedBalances[0]['cash']),
                        '$2,000' #+ '{:7,.2f}'.format(balances[index].combinedBalances[1]['cash'])
                        )
                )
    
    #tree.insert(acct.type[index], 'end',qtD.Accounts.isbilling+str(acct.number[index]), text = 'Is Billing: ' + str(acct.isBilling[index]))
    #tree.insert(acct.type[index], 'end', qtD.Accounts.isprimary+str(acct.number[index]), text = 'Is Primary: ' + str(acct.isPrimary[index]))
    #tree.insert(acct.type[index], 'end', qtD.Accounts.client_account_type+acct.number[index], text = 'Client Account Type: ' + acct.clientAccountType[index])


tree.bind("<ButtonRelease-1>", OnReleaseClick)


tree.column('#0',width=90)
tree.heading('#0', text='Type')
statuslabel = Label(root, bd=1, relief=SUNKEN, anchor=W)
statuslabel.config(text='test status bar', width =75)
statuslabel.grid(row=3, columnspan = 2)

root.update()
mainloop()


    

