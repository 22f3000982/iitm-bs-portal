from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Admin login ke liye session

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

    conn.close()

    if course:
        admin_mode = session.get('admin_mode', False)
        return render_template('course_detail.html', course_id=course_id, course_name=course[0], pyqs=pyqs, admin_mode=admin_mode)
    else:
        return "Course not found"

# Admin - Add PYQ
@app.route('/admin/add_pyq/<int:course_id>', methods=['GET', 'POST'])
def admin_add_pyq(course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    if request.method == 'POST':
        pyq_name = request.form['pyq_name']
        yt_link = request.form['yt_link']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO pyqs (course_id, name, yt_link) VALUES (?, ?, ?)', (course_id, pyq_name, yt_link))
        conn.commit()
        conn.close()

        return redirect(url_for('course_detail', course_id=course_id))

    return render_template('admin_add_pyq.html', course_id=course_id)

# Admin - Edit PYQ
@app.route('/admin/edit_pyq/<int:pyq_id>/<int:course_id>', methods=['GET', 'POST'])
def admin_edit_pyq(pyq_id, course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        new_name = request.form['pyq_name']
        new_link = request.form['yt_link']
        c.execute('UPDATE pyqs SET name = ?, yt_link = ? WHERE id = ?', (new_name, new_link, pyq_id))
        conn.commit()
        conn.close()
        return redirect(url_for('course_detail', course_id=course_id))

    c.execute('SELECT name, yt_link FROM pyqs WHERE id = ?', (pyq_id,))
    pyq = c.fetchone()
    conn.close()

    return render_template('admin_edit_pyq.html', pyq_id=pyq_id, course_id=course_id, pyq_name=pyq[0], yt_link=pyq[1])

# Admin - Delete PYQ
@app.route('/admin/delete_pyq/<int:pyq_id>/<int:course_id>')
def admin_delete_pyq(pyq_id, course_id):
    if not session.get('admin_mode'):
        return redirect(url_for('course_view'))

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM pyqs WHERE id = ?', (pyq_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('course_detail', course_id=course_id))

# ✅ New - Increment Watch Count
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

if __name__ == '__main__':
    if not os.path.exists('database.db'):
        init_db()
    else:
        init_db()

    app.run(debug=True)
