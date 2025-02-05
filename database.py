import os
from mysql.connector import connect, Error, errorcode

# Fetching credentials from environment variables
user = os.getenv('MYSQL_USER', 'root')  # defaulting to 'root' if not set
password = os.getenv('MYSQL_PASSWORD', 'MySQL2024Developement777')  # defaulting to a sample password
database = os.getenv('MYSQL_DATABASE', 'factory_kpi')  # defaulting to 'factory_kpi' if not set


def create_connection():
    """Creates and returns a database connection, and handles errors."""
    try:
        connection = connect(
            host="localhost",  # Add your host if different
            user=user,
            password=password,
            database=database
        )
        return connection
    except Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(e)
        return None

def query_data(connection):
    """Queries and prints data from a specified table."""
    cursor = connection.cursor()
    try:
        # Make sure to replace 'your_table_name' with the actual name of the table you want to query
        cursor.execute("SELECT * FROM production")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print("Error querying data: ", e)
    finally:
        cursor.close()



def close_connection(connection):
    """Closes the given database connection."""
    if connection:
        connection.close()

# Example usage
if __name__ == "__main__":
    conn = create_connection()
    if conn:
        # Here you might call your functions, e.g., query_data(conn)
        query_data(conn)  # Sample call to test query functionality Sample data insertion call
        close_connection(conn)
