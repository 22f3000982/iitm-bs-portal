import psycopg2

def admin_add_course(course_name):
    try:
        # Connect to your PostgreSQL database
        conn = psycopg2.connect(
            dbname="your_dbname",     # replace with your database name
            user="your_username",     # replace with your username
            password="your_password", # replace with your password
            host="localhost",         # or the relevant host for your database
            port="5432"               # or the port where your PostgreSQL is running
        )
        
        # Create a cursor object using a context manager to ensure it's closed after use
        with conn.cursor() as c:
            # Insert the course name into the courses table
            c.execute('INSERT INTO courses (name) VALUES (%s)', (course_name,))
            
            # Commit the transaction
            conn.commit()
            print("Course added successfully")
    
    except Exception as e:
        # In case of any errors, print the error message
        print(f"Error occurred: {e}")
    
    finally:
        # Close the connection
        if conn:
            conn.close()

# # Example usage
# course_name = "Business Analytics"  # You can change this to any course name
# admin_add_course(course_name)
