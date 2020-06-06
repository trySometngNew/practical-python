# pcost.py
# 
# Exercise 1.27
total_shares_cost = 0.0

with open('Data/portfolio.csv', 'rt') as f:
    header = next(f);
    for line in f:
        share_entry_list = line.split(',')
        share_cost = int(share_entry_list[1]) * float(share_entry_list[2])
        total_shares_cost = total_shares_cost + share_cost

print(f'Total Portfolio Value is ${total_shares_cost}')
