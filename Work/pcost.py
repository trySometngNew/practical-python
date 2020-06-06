# pcost.py
# 
# Exercise 1.32: Using a library function
def portfolio_cost(filename):
    import csv
    
    total_shares_cost = 0.0

    with open(filename, 'rt') as f:
    #     for line in f:
    #         print(line)
        rows = csv.reader(f)
        header = next(rows);
        missing_data = 0
        for row in rows:
            share_entry_list = row
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


cost = portfolio_cost('Data/portfolio.csv')
print(cost)