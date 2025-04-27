import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create courses table
c.execute('''
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Create pyqs table
c.execute('''
    CREATE TABLE IF NOT EXISTS pyqs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_id INTEGER,
        pyq_name TEXT NOT NULL,
        yt_link TEXT NOT NULL,
        FOREIGN KEY (course_id) REFERENCES courses(id)
    )
''')

conn.commit()
conn.close()

print("Database setup complete! ✅")
