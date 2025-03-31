# In the program a function named calculate_discount() is created.

#The function takes original price and discount_percent as parameters

#If discount is 20% or higher the discount is applied, else no discount

# The final price is printed as the output. 

def main():
    original_price = float(input("Enter the original price: $"))
    disc_percent = float(input("Enter the percent discount with no percent sign: "))
    final_price = calculate_discount(original_price, disc_percent)
    print(f"The final price is: ${final_price:.2f}")
    

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return (((100 - discount_percent)/100)*price)
    else:
        return price
    
main()