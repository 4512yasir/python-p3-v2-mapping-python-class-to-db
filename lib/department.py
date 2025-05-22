# lib/department.py

from lib import CURSOR, CONN

class Department:

    all = []

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location
        Department.all.append(self)

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"

    @classmethod
    def create_table(cls):
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY,
                name TEXT,
                location TEXT
            );
        """)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute("DROP TABLE IF EXISTS departments;")
        CONN.commit()

    def save(self):
        if self.id is None:
            CURSOR.execute("""
                INSERT INTO departments (name, location)
                VALUES (?, ?);
            """, (self.name, self.location))
            self.id = CURSOR.lastrowid
        else:
            self.update()
        CONN.commit()

    @classmethod
    def create(cls, name, location):
        department = cls(name, location)
        department.save()
        return department

    def update(self):
        CURSOR.execute("""
            UPDATE departments
            SET name = ?, location = ?
            WHERE id = ?;
        """, (self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        CURSOR.execute("""
            DELETE FROM departments
            WHERE id = ?;
        """, (self.id,))
        CONN.commit()
        Department.all.remove(self)

    @classmethod
    def get_all(cls):
        CURSOR.execute("SELECT * FROM departments;")
        rows = CURSOR.fetchall()
        return [cls(id=row[0], name=row[1], location=row[2]) for row in rows]
