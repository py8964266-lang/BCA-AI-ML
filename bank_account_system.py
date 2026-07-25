class BankAccount:
    def __init__(self,account_holder,account_number,mobile_number,balance,address):

        self.account_holder = account_holder
        self.account_number = account_number
        self.mobile_number = mobile_number
        self.__balance = balance
        self.address = address


    def show_details(self):

        print(f"The name of the Account holder is{self.account_holder}")
        print(f"Account number of the account holder is:{self.account_number}")
        print(f"Account holder mobile number is:{self.mobile_number}")        
        print(f"The address of the account holder is:{self.address}")

    def show_balance(self):
        print(f"The balance in the account holder is:{self.__balance}")  


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"You have successfully deposited {amount}.")


        else:  
            print(f"Invalid amount entered.")  

    def withdraw(self,amount):

        if (amount > 0) and (amount <= self.__balance):
            self.__balance -= amount
            print(f"You have withdraw the {amount} successfully.")
            print(f"current balance in your account is {self.__balance}")


        else:
            print("You have entered Invalid amount for withdrawn.")

class SavingAccount(BankAccount):
    def __init__(self,account_holder,number,mobile_number,balance,address,interest):

        super().__init__(account_holder,number,mobile_number,balance,address)

        self.interest = interest

class CurrentAccount(BankAccount):

    def __init__(self,account_holder,number,mobile_number,balance,address,overdraft):

        super().__init__(account_holder,number,mobile_number,balance,address)  

        self.overdraft = overdraft 
