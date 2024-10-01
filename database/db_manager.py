import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os


load_dotenv()

def create_database_if_not_exists():
   
    try:
        # Connect to MySQL server (without specifying a database)
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
           
        )
        
        if conn.is_connected():
            cursor = conn.cursor()
            db_name = os.getenv("DB_NAME")
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database `{db_name}` is ready.")
        
        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

def get_db_connection():

    create_database_if_not_exists()
    
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        auth_plugin='caching_sha2_password'
    )
    return conn

def get_user_by_id(user_id):
    # Retrieve user details from the MySQL database using a user ID
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT pin, fingerprint_template FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        # Return user details as a dictionary
        return {'pin': user[0], 'fingerprint_template': user[1]}
    return None

def save_user(pin, fingerprint_template):
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (pin, fingerprint_template) VALUES (%s, %s)", (pin, fingerprint_template))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    save_user('1234', 'fingerprint_template_example')

    # Example: Retrieve user
    user = get_user()
    if user:
        print(f"User PIN: {user['pin']}, Fingerprint Template: {user['fingerprint_template']}")
    else:
        print("No user found.")
