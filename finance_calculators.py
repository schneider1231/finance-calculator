import math

def cal_interest():
    """
    Calculates Interest depending on the type chosen: Simple or Compound
    """
    while True:
        try:
            deposit = float(input("How much money is the deposit amount? "))
            interest_rate = float(input("How much is the interest rate? "))
            interest_rate = interest_rate / 100
            years = float(input("How many years do you plan to invest? "))
            interest_type = input("Would you like 'simple' or 'compound' interest? Enter either 'simple' or 'compound': ").lower()

            if interest_type == "simple":
                user_investment = deposit * (1 + interest_rate * years)
                print(f"Your amount is {round(user_investment)}")
            elif interest_type == "compound":
                user_investment = deposit * math.pow((1 + interest_rate), years) 
                print(f"Your amount is {round(user_investment)}")
            else:
                print("ERROR: You didn't enter 'simple' or 'compound'")
        except ValueError:
            print("ERROR: Please enter a valid numeric value.")


def cal_bond():
    """
    Calculates The Loan repayment for a house 
    """
    while True:
        try:
            house_value = float(input("How much is the value of the house? "))
            interest_rate = float(input("How much is the interest rate? "))
            interest_rate = (interest_rate / 100) / 12
            months = float(input("How many months do you plan on repaying the bond? "))
            repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months))
            print(f"Your monthly repayment is {round(repayment)}")
        except ValueError:
            print("ERROR: Please enter a valid numeric value.")


def main():
    """
    Gets an input from the user to choose between either interest or bond 
    """
    print("investment - to calculate the amount of interest you'll earn on your investment")
    print("bond       - to calculate the amount you'll have to pay on a home loan")
    
    # User enters bond or investment
    while True:
        user_ans = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        if user_ans == "investment":
            cal_interest()
            break
        elif user_ans == "bond": 
            cal_bond()
            break
        else:
            print("ERROR: You didn't choose 'investment' or 'bond'")



main()
