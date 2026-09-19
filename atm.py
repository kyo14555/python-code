money=0
def Readmoney():
    print(f"Your balance is {money}.")

def Addmoney():
    global money
    print("Please enter the deposit amount.")
    addition=int(input())
    money+=addition
    print(f"Finish.Your current balance is {money}.")

def Withdrawmoney():
    global money
    print("Please enter your withdrawal money.")
    withdrawal=int(input())
    while withdrawal>money:
        print("Insufficient balance.")
        withdrawal=int(input())
        if withdrawal<=money:
            money-=withdrawal
            print(f"Finish.Your current balance is {money}.")
            break
    if withdrawal<=money:
            money-=withdrawal
            print(f"Finish.Your current balance is {money}.")
            

def Exit():
    print("Thanks for using.")

print("Welcome to ATM system.")
print("**********************")
print("***1.Balance inquiry**")
print("***2.Deposit**********")
print("***3.Withdraw*********")
print("***0.Exit*************")
print("**********************")
print("Please input your command.")

while True:
    cmd=input()
    if cmd=="1":
        Readmoney()
    if cmd=="2":
        Addmoney()
    if cmd=="3":
        Withdrawmoney()
    if cmd=="0":
        Exit()
        break