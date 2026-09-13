pin=123456
balance=50000
def login():
        password=int(input("enter your pin:"))
        if pin==password:
            print("ALLOW ACCESS")
            return True
        else:
            print("invalid pin")
            return False

def check_balance():
        print("balance",":",balance)
def deposit():
        global  balance
        amount=int(input("enter your deposited amount:"))

        if amount<=0:
            print("Money cannot be negative")

        balance+=amount
        print("money deposited successfully")
def withdraw():
        global  balance
        
        amount=int(input("enter your withdrawl amount:"))
        if amount>balance:
            print("Insufficient funds")
            balance-=amount
if login():
      check_balance()
      deposit()
      check_balance()
      withdraw()
      check_balance()

        