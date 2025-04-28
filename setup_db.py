import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

# PYQs table में watch_count add करो
try:
    c.execute('ALTER TABLE pyqs ADD COLUMN watch_count INTEGER DEFAULT 0')
except:
    print('pyqs में watch_count पहले से है या कुछ और issue है')

# Notes table में watch_count add करो
try:
    c.execute('ALTER TABLE notes ADD COLUMN watch_count INTEGER DEFAULT 0')
except:
    print('notes में watch_count पहले से है या कुछ और issue है')

# Assignments table में watch_count add करो
try:
    c.execute('ALTER TABLE assignments ADD COLUMN watch_count INTEGER DEFAULT 0')
except:
    print('assignments में watch_count पहले से है या कुछ और issue है')

conn.commit()
conn.close()

print("Done ✅")
