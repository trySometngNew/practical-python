# mortgage.py
#
# Exercise 1.9
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
bonus_per_month = 1000
bonus_duration = 12
month = 0
extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    if (principal * (1+rate/12) - payment) > 0:
        principal = principal * (1+rate/12) - payment
    else :
        principal = 0
    
    if month >= extra_payment_start_month and month <= extra_payment_end_month :
        if principal - bonus_per_month > 0 :
            principal = principal - bonus_per_month
        else : 
            principal = 0
        bonus_duration = bonus_duration - 1
        total_paid = total_paid + bonus_per_month
    else:
        pass
    total_paid = total_paid + payment
    print(month, total_paid, principal)

print('Total paid', total_paid)
print('month', month)