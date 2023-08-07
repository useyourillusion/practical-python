# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extramonths = 12
extra_payment = 1000
extra_payment_start_month = 61
extra_payment_end_month = 108

month = 0

while principal > 0:
    month += 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    if principal < 0:
        total_paid += principal
        principal = 0

    print(month, total_paid, principal)

print('Total paid', f"{round(total_paid,2):,}")
print('Months ', month)
