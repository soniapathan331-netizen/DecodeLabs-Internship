import string
import secrets
import math

def generate_password():
    # --- PHASE 1: INPUT ---
    while True:
        try:
            length = int(input("Enter password length (min 8): "))
            if length < 8:
                print("Minimum 8 characters required!")
            else:
                break
        except ValueError:
            print("Invalid input! Enter a number.")

    # --- PHASE 2: PROCESS ---
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # secrets.choice = cryptographically secure
    # list + join = memory efficient O(N)
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # --- PHASE 3: OUTPUT ---
    entropy = length * math.log2(len(characters))
    
    print(f"\n✅ Generated Password : {password}")
    print(f"🔒 Entropy            : {entropy:.2f} bits")
    
    # Strength rating
    if entropy >= 100:
        print("💪 Strength: VERY STRONG")
    elif entropy >= 60:
        print("👍 Strength: STRONG")
    else:
        print("⚠️  Strength: WEAK — increase length!")

generate_password()