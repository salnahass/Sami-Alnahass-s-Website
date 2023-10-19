# A. Import the sqlite library
import sqlite3

databaseName = "projects.db"

# B. From the objects.py containing our classes for this application,
#    only import the Movie class
# from objects import Movie

########################################################################################

#-------------------------------------
# 1. DELETE MOVIE FROM DB by Title
#-------------------------------------
def delProj_Title_DB(title):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect(databaseName)

    #B. Write a SQL statement to delete a specific row (based on Title name)
    sql='DELETE FROM movies WHERE Title=?'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (title,))

    # D. Save the changes
    conn.commit()


#-------------------------------------
# 2. ADD MOVIE FROM DB
#-------------------------------------
def saveProjectDB(Title, Description, ImageFileName):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect(databaseName)

    #B. Write a SQL statement to insert a specific row (based on Title name)
    sql='INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (Title,Description,ImageFileName, ))

    # D. Save the changes
    conn.commit()
    if conn:
        conn.close()

#-------------------------------------
# 3. Get single movie
#-------------------------------------
def getSingleDictList_DB(ID):
    conn = sqlite3.connect(databaseName)
    conn.row_factory = sqlite3.Row
    cursorObj = conn.cursor()
    project = []
    cursorObj.execute('SELECT * FROM projects where ID = ?;',(ID,))
    rows = cursorObj.fetchall()
    for row in rows:
        m = {"ID" : row["ID"], "Name" : row["Title"], "Year" : row["Description"], "ImageFileName" : row["ImageName"]  }
        project.append(m)
    return project

#-------------------------------------
# 4. UPDATE MOVIE FROM DB
#-------------------------------------
def updateProjectDB(ID, name, description, ImageFileName):
    #A. Make a connection to the database
    conn = None
    conn = sqlite3.connect(databaseName)

    #B. Write a SQL statement to insert a specific row (based on Title name)
    sql='UPDATE movies set Title = ?, Description=?, ImageFileName = ? where ID = ?'

    # B. Create a workspace (aka Cursor)
    cur = conn.cursor()

    # C. Run the SQL statement from above and pass it 1 parameter for each ?
    cur.execute(sql, (name,description, ImageFileName, ID))

    # D. Save the changes
    conn.commit()

#-------------------------------------
# 5. DELETE MOVIE FROM DB by ID
#-------------------------------------
def delMovies_DB(ID):
    conn = None
    conn = sqlite3.connect(databaseName)
    sql='DELETE FROM Movies WHERE ID=?'
    cur = conn.cursor()
    cur.execute(sql, (ID,))
    conn.commit()

#-------------------------------------
# 6. GET ALL MOVIES
#-------------------------------------
def getAllMovies():
    # A. Connection to the database
    conn = sqlite3.connect(databaseName)

    #------------------------------------------------------------------------
    # CHANGED LINE OF CODE BELOW
    #------------------------------------------------------------------------
    # A1. Add in row_factory.  This will allow us to use column names instead
    #     of guess which column position number our data is in
    conn.row_factory = sqlite3.Row

    # B. Create a workspace (aka Cursor)
    cursorObj = conn.cursor()

    # D. Run the SQL Select statement to retive the data
    cursorObj.execute('SELECT ID, Title, Description, ImageFileName FROM movies FROM projects;')

    # E. Tell Pyton to 'fetch' all of the records and put them in
    #     a list called allRows
    allRows = cursorObj.fetchall()

    projectList = []

    for individualRow in allRows:
        #m = {"Name" : individualRow[0], "Year": individualRow[1] }
        #------------------------------------------------------------------------
        # CHANGED CHANGED CHANGED CHANGED CHANGED CHANGED CHANGED CHANGED CHANGED
        #------------------------------------------------------------------------
        # The below technique uses column name instead of the position of the column
        # which could change if anyone modifies the SQL or the Table structure
        m = {"id" : individualRow["id"], "Title" : individualRow["Title"], "Year": individualRow["Description"], "ImageName": individualRow["ImageFileName"] }
        projectList.append(m)
    return projectList
