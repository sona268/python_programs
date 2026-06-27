class InsufficientBalanceError(Exception):
    pass
balance=25000
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    try:
        choice=int(input("Enter Choice: "))
        if choice==1:
            try:
                deposit=int(input("Enter Deposit Amount: "))
                if deposit<0:
                    raise ValueError("Negative amount is not allowed")
                    balance+=deposit
            except ValueError as e:
                print("ValueError:")
                print("Please enter a valid numeric amount")
        elif choice==2:
            try:
                withdrawal=int(input("Enter Withdrawal Amount: "))
                if withdrawal>balance:
                    raise InsufficientBalanceError("Insufficient Balance")
                balance-=withdrawal
            except InsufficientBalanceError as e:
                print("Exception Occurred:")
                print("InsufficientBalanceError:")
                print("InsufficientBalance")
                print("Transaction Failed")
        elif choice==3:
            print("Current Balance: ",balance)
            print("Transaction Successful")
            print("Thank You For Using ATM Banking System")
            print("Session Closed Successfully")
            break
    except Exception:
        print("Unexpected Error")