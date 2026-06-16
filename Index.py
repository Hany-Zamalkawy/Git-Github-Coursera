def calculate_simple_interest():
    print("--- Simple Interest Calculator ---")
    
    # Get user inputs
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time (in years): "))
    
    # Calculate interest
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    
    # Display results
    print(f"\nResults:")
    print(f"Interest Earned: ${interest:.2f}")
    print(f"Total Balance: ${total_amount:.2f}")

if __name__ == "__main__":
    calculate_simple_interest()