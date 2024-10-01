# app.py
from database.db_manager import get_user_by_id

def verify_pin(stored_pin, entered_pin):
    return stored_pin == entered_pin

def main():
    print("ATM Validation System")

    user_id = input("Weka ID We Mzee")
    pin = input("Enter PIN: ")
    

    user = get_user_by_id(user_id)
    
    # Check if user is found in the database
    if user:
        print(f"User's stored PIN: {user['pin']}")
        
        # Verify the entered PIN with the stored one
        if verify_pin(user['pin'], pin):
            print("logged successfully.")
        else:
            print("Invalid PIN.")
    else:
        print("No user found in the database. Please register a user.")

if __name__ == "__main__":
    main()
