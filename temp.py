# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

##Exercise_2

class BankAccount:
    
    def __init__(self, name, account_id, adress, income, balance=0):
            self.name=name
            self.account_id=account_id
            self.adress=adress
            self.income=income
            self.balance=balance
        
    def __str__(self):
        return f"{self.name}'s adress is: {self.adress}"
    
    def addMoney(self):
        return self.balance

x1=BankAccount("Adi", "315946681", "Naharriya", "100,000", balance=100)
x2=BankAccount("Tal","123" , "Hertzeliya", "10,000")       

print(x1)
print(x2)

x1.addMoney()
