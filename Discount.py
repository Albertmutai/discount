def calculate_discount(price, discount_percent):
    # Check if the discount percentage is 15% or higher
    if discount_percent >= 15:
        # Calculate the discounted price
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # If discount is less than 20%, return the original price
        return price

# Prompt the user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the calculate_discount function
final_price = calculate_discount(original_price, discount_percent)

# Display the result

if final_price == original_price:
    print(f"Not discounted. Final Price: ${final_price}")
else:
    print(f"Discount applied. Final Price after {discount_percent}% off: ${final_price}")
