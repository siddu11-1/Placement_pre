import sqlite3
from pathlib import Path
import datetime

DB_PATH = Path(__file__).parent / 'applications.db'

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS applications (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company TEXT NOT NULL,
        role TEXT,
        applied_date TEXT,
        status TEXT,
        source TEXT,
        location TEXT,
        notes TEXT,
        followup_date TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def add_application(company, role='', applied_date=None, status='Applied', source='', location='', notes='', followup_date=None):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO applications (company, role, applied_date, status, source, location, notes, followup_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (company, role, applied_date, status, source, location, notes, followup_date))
    conn.commit()
    conn.close()

def get_all():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute('SELECT * FROM applications ORDER BY created_at DESC')
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]
