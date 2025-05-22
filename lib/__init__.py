# lib/__init__.py

import sqlite3

CONN = sqlite3.connect('department.db')
CURSOR = CONN.cursor()
