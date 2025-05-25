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
        self.cursor = self.connection.cursor(dictionary=True)
        return self.cursor

    def closeAll(self):
        self.cursor.close()
        self.connection.close()

    def getAll(self):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM tasks ORDER BY due_date;")
        results = cursor.fetchall()
        self.closeAll()
        for task in results:
            task['done'] = bool(task['done'])
        return results

    def findByID(self, id):
        cursor = self.getcursor()
        cursor.execute("SELECT * FROM tasks WHERE id = %s;", (id,))
        result = cursor.fetchone()
        self.closeAll()
        if result:
            result['done'] = bool(result['done'])
        return result

    def create(self, task):
        cursor = self.getcursor()
        sql = """
            INSERT INTO tasks (title, description, due_date, done)
            VALUES (%s, %s, %s, %s);
        """
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
            UPDATE tasks
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
        cursor.execute("DELETE FROM tasks WHERE id=%s;", (id,))
        self.connection.commit()
        self.closeAll()

tasksDAO = TasksDAO()
