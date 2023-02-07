#!/user/bin/env python
# _*_coding=utf-8_*_
# Turtle Trading System
# Initialize the short and long moving averages
short_ma = 20
long_ma = 55

# Initialize the stop-loss and profit-taking levels
stop_loss = 10
profit_taking = 10

# Initialize a flag to indicate when a position is open
position_open = False

# Initialize variables to track entry/exit points
entry_price = 0.0
exit_price = 0.0

# Iterate through all prices
for price in prices:
    # Calculate the short moving average
    short_ma = calculate_moving_average(prices, short_ma)

    # Calculate the long moving average
    long_ma = calculate_moving_average(prices, long_ma)

    # Check if the short MA has crossed above the long MA
    if short_ma > long_ma and not position_open:
        # Buy at current price
        entry_price = price

        # Set the position open flag
        position_open = True

    # Check if the short MA has dropped below the stop-loss level
    if position_open and (short_ma - entry_price) < -stop_loss:
        # Sell at current price
        exit_price = price

        # Reset the position open flag
        position_open = False

    # Check if the short MA has crossed above the profit-taking level
    elif position_open and (short_ma - entry_price) > profit_taking:
        # Sell at current price
        exit_price = price

        # Reset the position open flag
        position_open = False