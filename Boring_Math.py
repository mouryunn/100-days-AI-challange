# 1. We define the Function (The Robot)
# We name it "calculate_total"
# The Arguments (Ingredients) are the 'price' and the 'tax'
def calculate_total(price, tax):
    
    # The robot does the math inside:
    tax_amount = price * tax
    final_price = price + tax_amount
    
    # 2. The Return Value (The Result)
    # The robot gives us back the final answer
    return final_price

# --- Now, let's use our Function! ---

# Let's say a video game costs $50.00 and tax is 0.08 (8%)
# We just give these numbers to our function:
my_total = calculate_total(50.00, 0.08)

# Print the answer
print("The total cost is:")
print(my_total)