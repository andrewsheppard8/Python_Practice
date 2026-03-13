"""Write a function to hide a credit card number. Takes credit card number and replaces all digits w * except the last four. so 1122334444 would be ******4444"""
# def functiona(parameter):
#     s=str(parameter)
#     return "*" * (len(s)-4) + s[-4:]
# print(functiona(11223355554444))

"""calling functions as objects"""
# def greet():
#     print("Hello")

# def run(func):
#     func()

# run(greet)

"""calling functions in functions"""
# def outer():
#     def inner():
#         print("Hello from inner")
#     return inner
# f=outer()
# f()

"""Working with basic decorators"""
# def my_decorator(func):
#     def wrapper():
#         print("Before the function runs")
#         func()  # call the original function
#         print("After the function runs")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hello")

# say_hello()

"""Using 'issubset' to check if all characters are within a set"""
# def check(stra,strb):
#     print(set(stra).issubset(strb))
# check("aabc","abcd")

"""Capitalize every other letter in a string"""
# def uppercase(str):
#     # str_list=list(str)
#     # for index, item in enumerate(str_list):
#     #     if index%2==0:
#     #         str_list[index]=item.upper()
#     #     else:
#     #         str_list[index]=item.lower()
#     # return "".join(str_list)

#     # return "".join(c.upper() if i%2==0 else c.lower() for i,c in enumerate(str))

#     """alternative solution"""
#     result=[]
#     capital=True
#     for i in str:
#         if capital:
#             result.append(i.upper())
#         else:
#             result.append(i.lower())
#         capital=not capital #flips t/f
#     return "".join(result)

# print(uppercase("bob")) #BoB

"""organize letters alphabetically"""
# x=["aa","cb","de","ze","ee"]
# # x.sort()
# y=sorted(x)
# print(y)

"""working with classes"""
# class Dog:

#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed

#     def bark(self):
#         return f"{self.name} says hi!"
    
#     def groom(self):
#         return f"{self.name} is getting groomed!"

# fluffy = Dog("Rusty","Poodle")
# print(fluffy.bark())
# print(fluffy.groom())

"""classes practice"""
# class BankAccount:
#     def __init__(self,owner,balance=0):
#         self.owner=owner
#         self.balance=balance
#         #create transaction log
#         self.transactions=[]
    
#     #all instances must take self as the first parameter
#     def deposit(self,amount):
#         self.balance += amount
#         self.transactions.append(f"Deposited ${amount}")
#         print(f"Added ${amount} to account. New balance: ${self.balance}")
    
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient funds!")
#         else:
#             self.balance -= amount
#             self.transactions.append(f"Withdrew ${amount}")
#             print(f"Withdrew ${amount}. New balance: ${self.balance}")

#     #converts the object to a string
#     def __str__(self):
#         return f"Owner {self.owner}, Balance: {self.balance}"
    
#     def show_transactions(self):
#         print("Transaction history: ")
#         for i in self.transactions:
#             print(i)


# bob=BankAccount("Bob")
# bob.deposit(100)
# bob.withdraw(50)
# print(bob)
# bob.show_transactions()

# name=input("Enter owner name: ")
# initial_balance=float(input("Enter starting balance: "))
# user_account=BankAccount(name, initial_balance)

# #while True used so code won't stop on its own
# while True:
#     action=input("Do you want to deposit, withdraw, show, or quit?").lower()
#     if action=="deposit":
#         amt=float(input("Amount to deposit: "))
#         user_account.deposit(amt)
#     elif action=="withdraw":
#         amt=float(input("Amount to withdraw: "))
#         user_account.withdraw(amt)
#     elif action=="show":
#         print(user_account)
#         user_account.show_transactions()
#     elif action=="quit":
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid option")



"""nesting ranges for output"""
# for i in range(0,3):
#     #resets every time
#     p=1
#     for j in range (i,5):
#         print(p,end=" ")
#         p=p+1
#     print()

"""string of text, how many times each occurs, give dictionary of only those that occur more than once, give dictionary/number of times they occur"""
# def string_check(strng):
#     word_count={}
#     #accounts for upper/lower case together
""".split() will always split into words, no need to define the space"""
#     for word in strng.lower().split():
#         word_count[word]=word_count.get(word,0)+1
#     # # print(word_count)
#     # for word,count_a in word_count.items():
#     #     if count_a > 1:   
#     #         print (f"{word},{count_a}")
#     filtered={word:count for word,count in word_count.items() if count > 1}
#     return filtered

# print(string_check("The CAT cat ran away"))

"""Check how many times each character occurs in string, practicing .get()"""
# def get_practice(strng):
#     # #will only give index value, not count
#     # character_count={char:i for i,char in enumerate(strng)}
#     # print(character_count)
#     char_cnt={}
#     for i in strng.lower():
#         #will only check values a-z, no numbers or special characters
#         if i.isalpha():
#             char_cnt[i]=char_cnt.get(i,0)+1
#     print(char_cnt)

# get_practice("bAnana!!!")