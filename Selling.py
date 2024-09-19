'''
A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
Ans:
'''
# Function to calculate profit or loss
def calculate_profit_loss(total_cost, sold_price_per_banana):
    # Cost per banana
    cost_per_banana = total_cost / 12
    # Total selling price for a dozen bananas
    total_selling_price = sold_price_per_banana * 12

    # Calculate profit or loss
    profit_loss = total_selling_price - total_cost

    # Determine the output format based on profit or loss
    if profit_loss > 0:
        return f"Profit : Rs.{profit_loss:.2f}"
    elif profit_loss < 0:
        return f"Loss : Rs.{abs(profit_loss):.2f}"
    else:
        return "No Profit No Loss"

# Input
X = float(input())
Y = float(input())

# Output
result = calculate_profit_loss(X, Y)
print(result)
