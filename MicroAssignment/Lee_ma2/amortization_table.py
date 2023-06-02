###
# Amortization Table
# Author: Nam Jun Lee
# Date: Sept 16th, 2021
###

# function for monthly loan amount
def monthly_loan(p, r, n):
    loan_amount = (r * p) / (1 - (1 + r) ** (-n))
    return loan_amount


# function for monthly interest amount
def monthly_interest(remain_p, loan_amount):
    interest = float(remain_p * loan_amount)
    return interest


# function for monthly principal
def monthly_principal(loan_amount, interest):
    month_p = loan_amount - interest
    return month_p


# Loan class
class Loan:
    # class fields
    P = 0
    R = 0
    N = 0

    # regular schedule method
    def regular_schedule(self):

        # Each item in the list is a tuple
        # Write header row with column names separated by tab
        tup = (" Month\t  ", " Starting_Balance\t  ",
               " Monthly_Payment\t", " Principal_Payment\t",
               " Interest_Payment\t", "  Ending_Balance")

        # remaining balance
        remain_bal = self.P

        # print each item in the list in terminal
        print("\nMonth", "Starting_Balance",
              "Monthly_Payment", "Principal_Payment",
              "Interest_Payment", "Ending_Balance\n")

        # create regular_schedule.csv file
        f = open('regular_schedule.csv', 'w')
        # write results from file
        f.writelines(tup)
        f.write('\n')
        for i in range(1, int(self.N) + 1):
            # starting principal balance
            start_bal = remain_bal
            # monthly payment
            month_pay = monthly_loan(self.P, self.R, self.N)
            # interest payment
            interest = monthly_interest(remain_bal, self.R)
            # principal payment
            principal = monthly_principal(month_pay, interest)
            # ending principal balance
            remain_bal = remain_bal - principal
            # show result in terminal
            print(i, round(start_bal, 2), round(month_pay, 2),
                  round(principal, 2), round(interest, 2), round(remain_bal, 2))
            # Write each tuple from the loan payment schedule list with tuple elements separated by tab
            # rounded to 2 decimal places and displayed with a $.
            f.writelines(str(i))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(start_bal, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(month_pay, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(principal, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(interest, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(remain_bal, 2)))
            f.write('\n')

        # close file
        f.close()

    # accelerated schedule method
    def accelerated_schedule(self, amount):

        # Each item in the list is a tuple
        # Write header row with column names separated by tab
        tup1 = (" Month\t  ", " Starting_Balance\t  ",
                " Monthly_Payment\t", " Principal_Payment\t",
                " Interest_Payment\t", "  Ending_Balance")

        # remaining balance
        remain_bal = self.P

        # print each item in the list in terminal
        print("\nMonth", "Starting_Balance",
              "Monthly_Payment", "Principal_Payment",
              "Interest_Payment", "Ending_Balance\n")

        # create accelerated_schedule.csv file
        f = open('accelerated_schedule.csv', 'w', newline='')
        # write results from file
        f.writelines(tup1)
        f.write('\n')
        for i in range(1, int(self.N) + 1):
            # starting principal balance
            start_bal = remain_bal
            # monthly payment
            month_pay = monthly_loan(self.P, self.R, self.N) + amount
            # interest payment
            interest = monthly_interest(remain_bal, self.R)
            # principal payment
            principal = monthly_principal(month_pay, interest)
            # ending principal balance
            remain_bal = remain_bal - principal
            # The number of items in the list should be less than or equal to the number of months for the loan
            if start_bal <= 0:
                break
            # show result in terminal
            print(i, round(start_bal, 2), round(month_pay, 2),
                  round(principal, 2), round(interest, 2), round(remain_bal, 2))
            # Write each tuple from the loan payment schedule list with tuple elements separated by tab
            # rounded to 2 decimal places and displayed with a $.
            f.writelines(str(i))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(start_bal, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(month_pay, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(principal, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(interest, 2)))
            f.write('   \t    ')
            f.write('$ ')
            f.writelines(str(round(remain_bal, 2)))
            f.write('\n')
        # close file
        f.close()


def main():
    # main program to prompt
    c = Loan()  # instance of Loan class in c
    input('What is this loan for? ')
    # principal (cost)
    c.P = input('Please enter the principal amount for the loan: ')
    c.P = float(c.P)
    # monthly interest rate
    c.R = input('Please enter the yearly interest rate (as a percent) for the loan: ')
    # enters to a decimal (divide by 100) and then dividing by 12 (12 months in a year)
    c.R = float(c.R) / 100 / 12
    # number of months
    c.N = input('Please enter the number of years for the loan: ')
    c.N = float(c.N) * 12  # change year to month
    # addition monthly amount
    toward = input('Additional monthly amount towards accelerated payment: ')
    toward = float(toward)
    # Call methods
    c.regular_schedule()
    c.accelerated_schedule(toward)


if __name__ == "__main__":
    main()
