class Atm:
    def __init__(self):
        self.pin=""
        self.balance=0
        self.menu()
    def menu(self):
        user_in=int(input("""
                  1.enter 1 to create pin
                  2.enter 2 to deposit
                  3.enter 3 to withdraw
                  4.enter 4 to check balance
                  5.enter 5 to exit \n"""))
        if user_in==1:
            self.createpin()
        elif user_in==2:
            self.deposit()
        elif user_in==3:
            self.withdraw()
        elif user_in==3:
            self.checkbalance()
        else:
            print("wrong")

    def createpin(self):
        self.pin=int(input("enter the pin to set\t"))
        print("pin set successfully\t")

                     
    def deposit(self):
        temp=int(input("enter your pin\t"))
        if temp==self.pin:
            amt=int(input("enter the amount you want to deposit\t"))
            self.balance=self.balance+amt
            print("deposit successful!!!\t")
        else:
            print("Invalid pin!! Please enter the correct pin\t")
    def withdraw(self):
        temp=int(input("enter your pin\t"))
        if temp==self.pin:
            amt=int(input("enter the amount you want to withdraw\t"))
            if amt<self.balance:
                self.balance=self.balance-amt
                print("withdraw successful!!!\t")
            else:
                print("Insufficient funds\t")
        else:
            print("Invalid pin!! Please enter the correct pin\t")


    def checkbalance(self):
        temp=int(input("enter your pin\t"))
        if temp==self.pin:
            print("Your Balnce is:\t", self.balance)
        
        
