import mysql.connector
import dbconfig as db

class TasksDAO:
    def __init__(self):
        self.host = db.mysql['host']
        self.user = db.mysql['user']
        self.password = db.mysql['password']
        self.database = db.mysql['database']

    def getcursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM Tasks ORDER BY due_date;")
        results = cursor.fetchall()
        tasks = [self.convertToDictionary(row) for row in results]
        self.closeAll()
        return tasks

    def findByID(self, id):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM Tasks WHERE id = %s;", (id,))
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDictionary(result) if result else None

    def create(self, task):
        cursor = self.getcursor()
        sql = """
            INSERT INTO Tasks (title, description, due_date, done)
            VALUES (%s, %s, %s, %s);
        """
        # Convert boolean done to int 0/1 for DB
        done_value = 1 if task.get('done', False) else 0
        values = (
            task.get('title'),
            task.get('description'),
            task.get('due_date'),
            done_value
        )
        cursor.execute(sql, values)
        self.connection.commit()
        task['id'] = cursor.lastrowid
        self.closeAll()
        return task

    def update(self, id, task):
        cursor = self.getcursor()
        sql = """
            UPDATE Tasks
            SET title=%s, description=%s, due_date=%s, done=%s
            WHERE id=%s;
        """
        done_value = 1 if task.get('done', False) else 0
        values = (
            task.get('title'),
            task.get('description'),
            task.get('due_date'),
            done_value,
            id
        )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, id):
        cursor = self.getcursor()
        cursor.execute("DELETE FROM Tasks WHERE id=%s;", (id,))
        self.connection.commit()
        self.closeAll()

    def convertToDictionary(self, row):
        keys = ['id', 'title', 'description', 'done', 'due_date', 'created_at', 'category_id', 'project_id', 'assigned_user_id']
        task_dict = {keys[i]: row[i] for i in range(len(keys))}
        
        task_dict['done'] = bool(task_dict['done'])
        return task_dict

tasksDAO = TasksDAO()
