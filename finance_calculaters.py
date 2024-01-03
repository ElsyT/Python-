import math # I have no idea what this is for. Please provide an explanation.

print (" investment - to calculate the amount of interest you'll earn on your investment\n"
       " bond - to calculate the amount you'll have to pay on a home loan\n")

finance_option = (input ("Enter either 'investment' or 'bond' from the menu above to proceed :\n")).lower()
if finance_option == "investment" :
    investment = float(input("Enter the amount of your depositing : "))
    rate = int(input("Enter the rate of interest : "))/100
    years = int(input("Enter the number of years you'd like to invest : "))
    type_of_interest =(input("Please select the type of interest 'simple' or 'compound':\n")).lower()
    if type_of_interest == "simple":
        total_interest = int(investment*(1+rate*years))
        print(f"This is the total interest : {total_interest}")
    elif type_of_interest == "compound":
        total_interest = int(investment * math.pow ((1+rate),years))
        print(f"This is the total interest : R{total_interest}")
    else:
        print("Unknown type of interest, please enter simple or compound:\n")

elif finance_option == "bond":
    value = float(input("Enter the present value of the house : "))
    rate_1 = int(input("Enter the rate of interest:"))/100
    rate = rate_1/12
    months= int(input("number of months to repay the bond : "))
    total_repayment= int(rate*value)/(1-(1+rate)**(-months))
    print(f"This is the total repayment : R {total_repayment} for the bond")
else :
    print("Please enter if you want investment or bond from menu above : \n")

'''Rrequest for client to choose between bond and investment: using the elif 
statement to determine which type of request has been made: and request appropriate information for future formulas. 
Request for type of interest: and calculate the formula for interest if a bond is chosen: request for appropriate information for future formulas, 
remembering to divide the rate by 12.'''