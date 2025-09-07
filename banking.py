import random
class BankAccount:
    promo_prize = 2000


    def __init__(self, name, balance, has_promo=False, isAdmin=False, isfrezze=False, messaging=False, message_type=[]):
        if has_promo == True:
            balance += self.promo_prize
        self.fullname=name
        self.account_nums=random.randint(100, 900)
        self.total_bal = balance
        self.Admin = isAdmin
        self.frozen= isfrezze
        self.inbox_type = message_type
        self.ismessage = messaging



    def notify(self,trans_type,amount):
        if self.ismessage == True:
            for choice in self.inbox_type:
                if choice == "SMS":
                    print( f"SMS: {trans_type} Alert of {amount} \n Account Name:{self.fullname}\n Account number:{self.account_nums}\n Account Balance: {self.total_bal}\n Thank you for banking with us")
                if choice == "E-MAIL":
                    print (f"E-MAIL {trans_type} Alert of {amount}\n Account Name: {self.fullname}\n Account number:{self.account_nums}\n if you did not approve of this E-Mail send us a message to freeze this account\nThank you for banking with us" )
        return "DONE"

    def frezze(self):
        if self.Admin == True:
            self.frozen= True
            return f"{self.account_nums} Your account has been frozen"
        else:
            return "You do not access to frezze this account"

    def unfrezze(self):
        if self.Admin == True:
            if self.frozen == True:
                self.frozen = False
                return "Account unfrezze sucessfully"
                
        else:
            return "You do not have access to unfrezze this account visit management for more enquries"


    def deposit(self, amount):
        if self.frozen:
            return self.frezze()
        else:
            if amount > 0:
                self.total_bal += amount
                print(self.notify("CREDIT", amount))
                return self.total_bal
            else:
                return "Invalid amount"

        
    def withdraw(self,amount):
        if self.frozen:
            return self.frezze()
        else:
            if amount <= self.total_bal:
                self.total_bal -= amount
                print(self.notify("DEBIT", amount))
                return"Withdraw sucessful"
            
            else:
                return "Insuffient funds"


    def transfer(self, recipent, amount):
        if amount <= self.total_bal:
            self.withdraw(amount)
            if TF == "Withdraw sucessful":
                print(self.notify("DEBIT", amount))
                recipent.deposit(amount)
                rprint(recipent.notify("CREDIT", amount))
                return "transfer sucessful"
            else:
                return "withdrawal not sucessful"
            
        else:
            return "Insuffient funds"

        
simon = BankAccount("stephen", 1000, isAdmin = True, messaging = True, message_type = ["SMS","E-MAIL"])
klaus = BankAccount("klaus", 4000)

print(simon.deposit(200))
print(simon.frezze())
print(simon.withdraw(200))
print(simon.unfrezze())
print(simon.withdraw(200))






