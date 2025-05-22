# lib/debug.py

from lib import CURSOR, CONN
from lib.department import Department
import ipdb

# Setup DB
Department.drop_table()
Department.create_table()

# Add some data
d1 = Department("Engineering")
d2 = Department("HR")
d1.save()
d2.save()

# Load all departments
departments = Department.get_all()
print(departments)

# Start interactive debugging session
ipdb.set_trace()
