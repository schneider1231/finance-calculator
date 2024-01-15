import math

investment = "investment"
bond = "bond"


print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
# user enters bond or investment
User_ans = input("""
Enter either 'investment' or 'bond' from the menu above to proceeed:""").lower()
# ask for investment details
if User_ans == investment:
    deposit = int(input("how much money is the deposit amount"))
    interest_rate = int(input("how much is the interest rate"))
    years = int(input("how many years do you plan to invest"))
    interest_type = input("would you like 'simple' or 'compound' interest Enter either 'simple' or 'compound' ").lower()
 #calculates simple interest amount   
    if interest_type == "simple":
         user_investment = deposit * (1 + interest_rate * years)
         print (f"your amount is {user_investment}")
#calculates compund interest         
    elif interest_type == "compound":
         user_investment = deposit * math.pow((1+interest_rate),years) 
         print (f"your amount is {user_investment}")    
#informs user they entered an incorrect input    
    else:
         print ("you didn't enter 'simple' or 'compound'")     
#ask for bond details and calculates monthly repayments
elif User_ans == bond:
     house_value = int(input("how much is the value of the house?"))
     interest_rate = int(input("how much is the interest rate?"))
     months = int(input("how many months do you plan on repaying the bond?"))
     repayment = (interest_rate * house_value)/(1-(1+interest_rate)**(-months))
     print (f"your monthly repayment is {repayment}")
else:
     print("ERROR you didnt choose 'investment' or 'bond'")     