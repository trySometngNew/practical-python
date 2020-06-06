# pcost.py
# 
# Exercise 1.30: Turning a script into a function
def portfolio_cost(filename):
    import gzip
    
    total_shares_cost = 0.0

    with open(filename, 'rt') as f:
    #     for line in f:
    #         print(line)
        header = next(f);
        for line in f:
            share_entry_list = line.split(',')
            share_cost = int(share_entry_list[1]) * float(share_entry_list[2])
            total_shares_cost = total_shares_cost + share_cost

    print(f'Total Portfolio Value is ${total_shares_cost}')
    return total_shares_cost


cost = portfolio_cost('Data/portfolio.csv')
print(cost)