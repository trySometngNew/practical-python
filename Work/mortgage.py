# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
bonus_per_month = 1000
bonus_duration = 12
month = 0

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    
    if bonus_duration > 0:
        principal = principal - bonus_per_month
        bonus_duration = bonus_duration - 1
    else:
        pass
    total_paid = total_paid + payment + bonus_per_month
print('Total paid', total_paid)
print('month', month)