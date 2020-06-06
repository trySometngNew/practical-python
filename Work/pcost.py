# pcost.py
# 
# Exercise 1.30: Catching and Handling Exceptions
def portfolio_cost(filename):
    import gzip
    
    total_shares_cost = 0.0

    with open(filename, 'rt') as f:
    #     for line in f:
    #         print(line)
        header = next(f);
        missing_data = 0
        for line in f:
            share_entry_list = line.split(',')
            try:                
                share_cost = int(share_entry_list[1]) * float(share_entry_list[2])
                total_shares_cost = total_shares_cost + share_cost
            except ValueError:
                missing_data = missing_data + 1
                pass
            except IndexError:
                missing_data = missing_data + 1
                pass

    print(f'Total Portfolio Value is ${total_shares_cost}')
    print(f'Missing Data count which has been skipped over is {missing_data}')
    return total_shares_cost


cost = portfolio_cost('Data/missing.csv')
print(cost)