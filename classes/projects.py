import sqlite3
class Project:
    def __init__(self, title="", description="", ):
        self.__title = title
        self.__description = description
        self.__imageFileName = imageFileName

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value

    @property
    def imageFileName(self):
        return self.__imageFileName

    @imageFileName.setter
    def imageFileName(self, value):
        self.__imageFileName = value

    @classmethod
    def saveProjectDB(cls, title, description, imageFileName):
        conn = sqlite3.connect('projects.db')
        sql = 'INSERT INTO projects (Title, Description, ImageFileName) values (?,?,?)'
        cur = conn.cursor()
        cur.execute(sql, (title, description, imageFileName))
        conn.commit()
        conn.close()

    @classmethod
    def getAllProjects(cls):
        conn = sqlite3.connect('projects.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Title, Description, ImageFileName FROM projects')
        allRows = cursor.fetchall()
        projectList = []
        for row in allRows:
            project = {"Title": row[0], "Description": row[1], "ImageFileName": row[2]}
            projectList.append(project)
        conn.close()
        return projectList
