import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Remove the 0012 migration that doesn't exist in Django 3.0
cursor.execute("DELETE FROM django_migrations WHERE app='auth' AND name='0012_alter_user_first_name_max_length'")
print(f"Removed {cursor.rowcount} invalid migration record(s)")

conn.commit()
conn.close()
print("Done!")
