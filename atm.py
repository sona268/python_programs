customer_name=input("Enter customer name: ")
card_number=input("Enter card number: ")
pin_number=int(input("Enter pin number: "))
account_type=input("Enter account type (Savings / Current): ")
available_balance=float(input("Enter available balance: "))
withdrawal_amount=float(input("Enter the withdrawal amount: "))


valid_account_type=["Savings","Current"]
if account_type in valid_account_type:
    print("Account available")
else:
    print("Account not available")


stored_pin=1234
pin_verified=pin_number==stored_pin
sufficient_balance=withdrawal_amount<=available_balance
initial_balance=available_balance>0
print("Pin verified: ",pin_verified)
print("Sufficient balance: ",sufficient_balance)
print("Balance greater than zero: ",initial_balance)


if pin_verified and account_type in valid_account_type and sufficient_balance:
    transaction_status="Successful"
    print("Withdrawal Successful")
else:
    transaction_status="Failed"
    print("Withdrawal Failed")


account1=account_type
account2=account_type
print("Account1 is account2: ",account1 is account2)
print("Account1 is not Account2: ",account1 is not account2)


remaining_balance=available_balance-withdrawal_amount
print("Remaining balance: ",remaining_balance)


remaining_balance+=0
remaining_balance-=0
remaining_balance*=1


print("Datatype of customer name: ",type(customer_name))
print("Datatype of card number: ",type(card_number))
print("Datatype of pin number: ",type(pin_number))
print("Datatype of account type: ",type(account_type))
print("Datatype of available balance: ",type(available_balance))
print("Datatype of withdrawal amount: ",type(withdrawal_amount))


print("Is available balance float?",isinstance(available_balance,float))
print("Is withdrawal amount float?",isinstance(withdrawal_amount,float))
print("Is customer name string?",isinstance(customer_name,str))


print("Id of available balance: ",id(available_balance))
print("Id of remaining balance: ",id(remaining_balance))
print("Id of account type: ",id(account_type))


print("----------- SMART ATM SYSTEM -----------")
print("Customer Name: ",customer_name)
print("Card Number: ",card_number)
print("Account Type: ",account_type)
print("Available Balance: ",available_balance)
print("Withdrawal Amount: ",withdrawal_amount)
print("Pin Verified: ",pin_verified)
print("Valid Account Type: ",account_type in valid_account_type)
print("Sufficient Balance: ",sufficient_balance)
print("Transaction Status: ",transaction_status)
print("Remaining Balance: ",remaining_balance)
print("Account1 is Account2: ",account1 is account2)
print("Account1 is not Account2: ",account1 is not account2)