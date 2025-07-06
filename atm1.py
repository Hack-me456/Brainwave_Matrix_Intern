balance = 10000
pin = "1234"

print("===== Welcome to the ATM =====")
print("1. Card")
print("2. Cardless")
print("==============================")

mode = input("Select mode (1 for Card, 2 for Cardless): ")

if mode == "1":  # Card Mode
    entered_pin = input("Enter your 4-digit PIN: ")

    if entered_pin == pin:
        print("PIN Verified Successfully.\n")

        while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("====================")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                print(f"Your current balance is: ₹{balance}\n")

            elif choice == "2":
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Invalid amount. Try again.")
                else:
                    balance += amount
                    print(f"₹{amount} deposited successfully.")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid amount. Try again.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"₹{amount} withdrawn successfully.")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please select 1-4.")
    else:
        print("Incorrect PIN. Access Denied!")

elif mode == "2":  
    mobile_number = input("Enter your registered mobile number: ")
 
    while True:
            print("\n===== ATM Menu =====")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            print("====================")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                print(f"Your current balance is: ₹{balance}\n")

            elif choice == "2":
                amount = float(input("Enter amount to deposit: ₹"))
                if amount <= 0:
                    print("Invalid amount. Try again.")
                else:
                    balance += amount
                    print(f"₹{amount} deposited successfully.")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == "3":
                amount = float(input("Enter amount to withdraw: ₹"))
                if amount <= 0:
                    print("Invalid amount. Try again.")
                elif amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= amount
                    print(f"₹{amount} withdrawn successfully.")
                    print(f"Updated Balance: ₹{balance}")

            elif choice == "4":
                print("Thank you for using the ATM!")
                break

            else:
                print("Invalid choice. Please select 1-4.")
    

else:
    print("Invalid mode selected.")
