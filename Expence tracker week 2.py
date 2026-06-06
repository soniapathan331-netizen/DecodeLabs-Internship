total = 0  # Accumulator - initialized OUTSIDE the loop

while True:
    user_input = input("Enter expense (or 'quit' to stop): ")
    
    if user_input == "quit":
        break  # Kill switch - exits the loop
    
    try:
        expense = int(user_input)  # Gatekeeper - converts string to number
        total = total + expense    # Accumulator pattern
        print(f"Added! Running total: {total}")
    
    except ValueError:
        print("Invalid input! Please enter a number.")

print(f"Final Total: {total}")  # Output phase