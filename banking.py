import random
class BankAccount:
    promo_prize = 2000


    def __init__(self, name, balance, has_promo=False, isAdmin=False, isfrezze=False, messaging=False, message_type="SMS"):
        if has_promo == True:
            balance += self.promo_prize
        self.fullname=name
        self.account_nums=random.randint(100, 900)
        self.total_bal = balance
        self.Admin = isAdmin
        self.frozen= isfrezze
        self.inbox_type = [message_type]
        self.ismessage = messaging



    def notify(self,trans_type,amount):
        if self.ismessage == True:
            for choice in self.inbox_type:
                if choice == "SMS":
                    return f"SMS: {trans_type} Alert of {amount} from {self.fullname}: {self.account_nums} Thank you for banking with us"
                if choice == "E-MAIL":
                    return f"E-MAIL {trans_type} \n Alert of {amount} from account details: {self.fullname}: {self.account_nums} \n if you did not approve this message send us a message to freeze this account \n Thank you for banking with us" 


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
                print(self.notify("CREDIT", amount))
                return self.total_bal
            else:
                return "Invalid amount"

        
    def withdraw(self,amount):
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

        
simon = BankAccount("stephen", 1000, isAdmin = True, messaging = True, message_type="SMS")
klaus = BankAccount("klaus", 4000)

print(simon.deposit(200))

print(simon.withdraw(200))






