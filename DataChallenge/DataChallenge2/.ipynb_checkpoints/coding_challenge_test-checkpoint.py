def max_profit_helper(price):
    max_out = 0
    
    # If there is less than one day of transaction
    if len(price) <= 1:
        return 0
    
    lowest_buy = price[0]
    for i in range(1,len(price)):
        max_out = max(max_out, price[i] - lowest_buy)
        lowest_buy = min(lowest_buy, price[i])
    
    return max_out


##DON"T CHANGE THIS
def max_profit(price):
    return max_profit_helper(price)

def main():
    test = [7, 1, 5, 3, 6, 4]
    
    print(max_profit(test))

if __name__ == "__main__":
    main()