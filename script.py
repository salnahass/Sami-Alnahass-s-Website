import sqlite3

#Connect to db

conn = sqlite3.connect("projects.db")



#Create cursor object which executes SQL command

cursor = conn.cursor()



#Write SQL statement which creates "projects" table

create_table_sql = """
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Description TEXT,
    ImageFileName TEXT
);
"""




#Execute SQL statement to create table

cursor.execute(create_table_sql)

#Commit the changes and close the connection

conn.commit()

conn.close()