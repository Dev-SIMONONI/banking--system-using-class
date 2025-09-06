'''
1:Create account(name,account_num,balance,)generate random account number, if user have promo bala +2000
'''
import random
class BankAccount:
    promo_prize = 2000

    
        

    def __init__(self, name, balance, has_promo=False, isAdmin=False, isfrezze=False, message_type="SMS"):
        if has_promo == True:
            balance += self.promo_prize
        self.fullname=name
        self.account_nums=random.randint(100, 900)
        self.total_bal = balance
        self.Admin = isAdmin
        self.frozen= isfrezze


    def frezze(self):
        if self.Admin == True:
            self.frozen= True
            return f"{self.account_nums} Your account has been frozen"
        else:
            return "You do not access to frezze this account"








    def deposit(self, amount):
        if self.frozen:
            return self.frezze()
        else:
            if amount > 0:
                self.total_bal += amount
                return self.total_bal
            else:
                return "Invalid amount"

        
    def withdraw(self,amount):
        if amount <= self.total_bal:
            self.total_bal -= amount
            return"Withdraw sucessful"
            
        else:
            return "Insuffient funds"


    def transfer(self, recipent, amount):
        if amount <= self.total_bal:
            self.withdraw(amount)
            if TF == "Withdraw sucessful":
                recipent.deposit(amount)
                return "transfer sucessful"
            else:
                return "withdrawal not sucessful"
            
        else:
            return "Insuffient funds"


    


        

    



simon = BankAccount("stephen", 1000, isAdmin = True)
klaus = BankAccount("klaus", 4000)


print(simon.deposit(200))
print(simon.frezze())
print(simon.deposit(200))



print(klaus.deposit(100))



