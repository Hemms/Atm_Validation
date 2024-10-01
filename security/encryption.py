# security/encryption.py
import bcrypt

# Function to hash a user's PIN securely
def hash_pin(pin):
    # Generate a salt and hash the PIN
    salt = bcrypt.gensalt()
    hashed_pin = bcrypt.hashpw(pin.encode('utf-8'), salt)
    return hashed_pin

# Function to verify if the entered PIN matches the stored hash
def verify_pin(stored_hashed_pin, entered_pin):
    # Check if the entered PIN matches the stored hashed PIN
    return bcrypt.checkpw(entered_pin.encode('utf-8'), stored_hashed_pin)
