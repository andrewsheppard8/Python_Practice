"""Creating the class"""
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
        #create transaction log
        self.transactions=[]
    
    #all instances must take self as the first parameter
    def deposit(self,amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")
        print(f"Added ${amount} to account. New balance: ${self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            print(f"Withdrew ${amount}. New balance: ${self.balance}")

    #converts the object to a string
    def __str__(self):
        return f"Owner {self.owner}, Balance: {self.balance}"
    
    def show_transactions(self):
        print("Transaction history: ")
        for i in self.transactions:
            print(i)


# bob=BankAccount("Bob")
# bob.deposit(100)
# bob.withdraw(50)
# print(bob)
# bob.show_transactions()

name=input("Enter owner name: ")
initial_balance=float(input("Enter starting balance: "))
user_account=BankAccount(name, initial_balance)

#while True used so code won't stop on its own
while True:
    action=input("Do you want to deposit, withdraw, show, or quit?").lower()
    if action=="deposit":
        amt=float(input("Amount to deposit: "))
        user_account.deposit(amt)
    elif action=="withdraw":
        amt=float(input("Amount to withdraw: "))
        user_account.withdraw(amt)
    elif action=="show":
        print(user_account)
        user_account.show_transactions()
    elif action=="quit":
        print("Goodbye!")
        break
    else:
        print("Invalid option")