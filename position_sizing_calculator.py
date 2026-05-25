def calculate_position_size(account_size, risk_percentage, entry_price, stop_loss_price):

  if stop_loss_price >= entry_price:
    # safety check : stop loss price should be less than entry price for long position.
    return {"error": "Stop loss must be less than entry price for buy order"}

  # calculate maximum cash allowed to risk
  cash_at_risk = account_size * (risk_percentage / 100)

  # Calculate the risk for single share
  risk_per_share = entry_price - stop_loss_price

  # Calculate total shares ( using // to run down nearest whole share)
  shares_to_buy = cash_at_risk // risk_per_share

  # Calculate total capital required to open this position
  total_cost = shares_to_buy * entry_price

  # Safety check : check if you have enough money to buy shares
  if total_cost > account_size:
    # if total cost exceeds account size value then we are limted by account size not by stop loss
    shares_to_buy = account_size // entry_price
    total_cost = shares_to_buy * entry_price
    max_risk_loss = shares_to_buy * risk_per_share # Recalculate max_risk_loss with new shares_to_buy
  else:
    # If total_cost is within account_size, use the initial calculations
    max_risk_loss = shares_to_buy * risk_per_share

  return {
      "Shares" : int(shares_to_buy),
      "Total_Investments" : round(total_cost, 2),
      "Max_risk_loss" : round(max_risk_loss, 2)
  }
""" Consider a scenario where we are having trade in TATA Steel with an entry price 210 Rs and stop loss of 208 Rs and if we have an account of 10000 Rs and max stop loss of 1.5 %"""
result = calculate_position_size(
  account_size = 10000,
  risk_percentage = 1.5,
  entry_price = 210,
  stop_loss_price = 208
)

print("-----Risk Management-----")

# Check if the function returned an error
if "error" in result:
  print(f"Error: {result['error']}")
else:
  print(f"Shares to buy : {result['Shares']} shares")
  print(f"Total capital required : {result['Total_Investments']} Rs") # Corrected key name
  print(f"Max loss if stop loss hits : {result['Max_risk_loss']} Rs")