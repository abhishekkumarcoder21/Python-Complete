class BankAccount:
    def __init__(self,account_number,account_balance):
        self.account_numebr=account_number
        # self.account_balance=account_balance --> this is public
        self.__account_balance=account_balance # become private variable due to the __

    def deposit(self,amount):
        self.__account_balance+=amount
        print(f"Deposited : {amount} | Current balamce : {self.__account_balance}")
    
    def get_balance(self):
        return self.__account_balance  # controlled access to the account balance
    

account=BankAccount('12345',100000)
account.deposit(50000)
print(account.get_balance())
# print(account.__account_balance()) --> we cannot directly access the account balance , but with the help of the function get_account_balance
