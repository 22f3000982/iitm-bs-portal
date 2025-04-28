from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Create tables if they don't exist
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create 'courses' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Create 'pyqs' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS pyqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT,
            watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')

    # Create 'notes' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT,
            watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')

    # Create 'assignments' table
    c.execute('''
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            yt_link TEXT,
            watch_count INTEGER DEFAULT 0,
            FOREIGN KEY (course_id) REFERENCES courses(id)
        )
    ''')

    conn.commit()
    conn.close()

# Home - Show all courses
@app.route('/', methods=['GET', 'POST'])
def course_view():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM courses')
    courses = c.fetchall()
    conn.close()

    admin_mode = session.get('admin_mode', False)
    return render_template('course_view.html', courses=courses, admin_mode=admin_mode)

# Admin login (password 4129)
@app.route('/admin_login', methods=['POST'])
def admin_login():
    password = request.form['password']
    if password == '4129':
        session['admin_mode'] = True
    return redirect(url_for('course_view'))

# Admin logout
@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_mode', None)
    return redirect(url_for('course_view'))

# Admin - Add course
@app.route('/admin/add_course', methods=['GET', 'POST'])
def admin_add_course():
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    if request.method == 'POST':
        course_name = request.form['course_name']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO courses (name) VALUES (?)', (course_name,))
        conn.commit()
        conn.close()
        return redirect(url_for('course_view'))

    return render_template('admin_add_course.html')

# Admin - Edit course
@app.route('/admin/edit_course/<int:course_id>', methods=['GET', 'POST'])
def admin_edit_course(course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        new_name = request.form['course_name']
        c.execute('UPDATE courses SET name = ? WHERE id = ?', (new_name, course_id))
        conn.commit()
        conn.close()
        return redirect(url_for('course_view'))

    c.execute('SELECT name FROM courses WHERE id = ?', (course_id,))
    course = c.fetchone()
    conn.close()

    return render_template('admin_edit_course.html', course_id=course_id, course_name=course[0])

# Admin - Delete course
@app.route('/admin/delete_course/<int:course_id>')
def admin_delete_course(course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM courses WHERE id = ?', (course_id,))
    c.execute('DELETE FROM pyqs WHERE course_id = ?', (course_id,))
    c.execute('DELETE FROM notes WHERE course_id = ?', (course_id,))
    c.execute('DELETE FROM assignments WHERE course_id = ?', (course_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('course_view'))

# View course detail
@app.route('/course/<int:course_id>')
def course_detail(course_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT name FROM courses WHERE id=?', (course_id,))
    course = c.fetchone()

    c.execute('SELECT id, name, yt_link, watch_count FROM pyqs WHERE course_id=?', (course_id,))
    pyqs = c.fetchall()

    c.execute('SELECT id, name, yt_link, watch_count FROM notes WHERE course_id=?', (course_id,))
    notes = c.fetchall()

    c.execute('SELECT id, name, yt_link, watch_count FROM assignments WHERE course_id=?', (course_id,))
    assignments = c.fetchall()

    conn.close()

    if course:
        admin_mode = session.get('admin_mode', False)
        return render_template('course_detail.html',
                               course_id=course_id,
                               course_name=course[0],
                               pyqs=pyqs,
                               notes=notes,
                               assignments=assignments,
                               admin_mode=admin_mode)
    else:
        return "Course not found"

# Admin - Add PYQ / Notes / Assignment
@app.route('/admin/add_item/<item_type>/<int:course_id>', methods=['GET', 'POST'])
def admin_add_item(item_type, course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    if request.method == 'POST':
        item_name = request.form['item_name']
        yt_link = request.form['yt_link']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        if item_type == 'pyqs':
            c.execute('INSERT INTO pyqs (course_id, name, yt_link) VALUES (?, ?, ?)', (course_id, item_name, yt_link))
        elif item_type == 'notes':
            c.execute('INSERT INTO notes (course_id, name, yt_link) VALUES (?, ?, ?)', (course_id, item_name, yt_link))
        elif item_type == 'assignments':
            c.execute('INSERT INTO assignments (course_id, name, yt_link) VALUES (?, ?, ?)', (course_id, item_name, yt_link))

        conn.commit()
        conn.close()
        return redirect(url_for('course_detail', course_id=course_id))

    return render_template('admin_add_pyq.html', course_id=course_id, item_type=item_type)

# ✅ Watch Count Increment (PYQs)
@app.route('/increment_watch/<int:pyq_id>')
def increment_watch(pyq_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE pyqs SET watch_count = watch_count + 1 WHERE id = ?', (pyq_id,))
    conn.commit()
    c.execute('SELECT yt_link FROM pyqs WHERE id = ?', (pyq_id,))
    link = c.fetchone()
    conn.close()

    if link:
        return redirect(link[0])
    else:
        return "Link not found"

# ✅ Watch Count Increment (Notes)
@app.route('/increment_watch_note/<int:note_id>')
def increment_watch_note(note_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE notes SET watch_count = watch_count + 1 WHERE id = ?', (note_id,))
    conn.commit()
    c.execute('SELECT yt_link FROM notes WHERE id = ?', (note_id,))
    link = c.fetchone()
    conn.close()

    if link:
        return redirect(link[0])
    else:
        return "Link not found"

# ✅ Watch Count Increment (Assignments)
@app.route('/increment_watch_assignment/<int:assignment_id>')
def increment_watch_assignment(assignment_id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('UPDATE assignments SET watch_count = watch_count + 1 WHERE id = ?', (assignment_id,))
    conn.commit()
    c.execute('SELECT yt_link FROM assignments WHERE id = ?', (assignment_id,))
    link = c.fetchone()
    conn.close()

    if link:
        return redirect(link[0])
    else:
        return "Link not found"

# Admin - Edit item (PYQ/Note/Assignment)
@app.route('/admin/edit_item/<string:item_type>/<int:course_id>/<int:item_id>', methods=['GET', 'POST'])
def admin_edit_item(item_type, course_id, item_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        new_title = request.form['title']
        new_link = request.form['link']

        if item_type == 'pyqs':
            c.execute('UPDATE pyqs SET name=?, yt_link=? WHERE id=?', (new_title, new_link, item_id))
        elif item_type == 'notes':
            c.execute('UPDATE notes SET name=?, yt_link=? WHERE id=?', (new_title, new_link, item_id))
        elif item_type == 'assignments':
            c.execute('UPDATE assignments SET name=?, yt_link=? WHERE id=?', (new_title, new_link, item_id))

        conn.commit()
        conn.close()
        return redirect(url_for('course_detail', course_id=course_id))

    # Fetch existing item
    if item_type == 'pyqs':
        c.execute('SELECT name, yt_link FROM pyqs WHERE id=?', (item_id,))
    elif item_type == 'notes':
        c.execute('SELECT name, yt_link FROM notes WHERE id=?', (item_id,))
    elif item_type == 'assignments':
        c.execute('SELECT name, yt_link FROM assignments WHERE id=?', (item_id,))
    
    item = c.fetchone()
    conn.close()

    if item:
        item_data = {
            'title': item[0],
            'link': item[1]
        }
        return render_template('admin_edit_item.html', item=item_data, item_type=item_type, course_id=course_id, item_id=item_id)
    else:
        return "Item not found"

# Admin delete item route
@app.route('/admin/delete_item/<string:item_type>/<int:course_id>/<int:item_id>', methods=['POST', 'GET'])
def admin_delete_item(item_type, course_id, item_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if item_type == 'pyqs':
        c.execute('DELETE FROM pyqs WHERE id=?', (item_id,))
    elif item_type == 'notes':
        c.execute('DELETE FROM notes WHERE id=?', (item_id,))
    elif item_type == 'assignments':
        c.execute('DELETE FROM assignments WHERE id=?', (item_id,))
    else:
        flash('Invalid item type.', 'error')
        return redirect(url_for('course_detail', course_id=course_id))

    conn.commit()
    conn.close()
    flash('Item deleted successfully!', 'success')
    return redirect(url_for('course_detail', course_id=course_id))

# Main
if __name__ == '__main__':
    if not os.path.exists('database.db'):
        init_db()
    else:
        init_db()

    app.run(debug=True)
