#Bank account Deposit.


class Bankaccount:
  	def __init__(self,__account_number,account _ holder_name,initial_balance=200.0);
	     self.__account_number=account_number
	     self.__account_holder_name=account_ holder name
	     self.__account_balance=initial balance
	     
	   def deposit(self,amount);
	     if   amount>0;
	         self.__account_balance+=amount
	         #self.__account_number=self.__account  balance+amount  
	         Print("Deposited  ₹{}.New balance:₹{}".format(amount,self.__ account_balanace))
	      
	     else:
	     	Print("Invalid deposit amount.Please deposit  a positive amount.")
	   
	 def withdraw(self,amount):
	 	if amount>0 and amount<=self.__account  balance-=amount
	 	#self.__account__number=self.__account balance-amount
	    	Print("withdraw  ₹{}.New balance:₹{}".format(amount,self.__account_balance))
	 	else:
	 		 Print("Invalid withdrawl amount or insufficient balance.")
	   
	   def display  balance(self):
	          Print("Account balance for{}(Account  #{}):₹{}".format ( self.__account_holder_name,   self.__account_number,self.__account_balance))
	         

# create an instance of the BankAccount	          	          
account=Bank Account(account  number="123456789",    account__holder_name="SOWMITHRA",initial  balance=5000.0)
                   
#Test deposit and withdrawl functionally:                  
account.display  balance()
account.deposit(500.0)
account.withdraw(200.0)
#account.display  balance{}	 		 
