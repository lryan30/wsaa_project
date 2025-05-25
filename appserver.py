from flask import Flask, render_template, request, jsonify, abort
from taskDAO import tasksDAO


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        tasks = tasksDAO.getAll()
        return jsonify(tasks)
    elif request.method == 'POST':
        data = request.get_json()
        if not data:
            abort(400, "Invalid JSON data")
        task = {
            'title': data.get('title'),
            'description': data.get('description'),
            'due_date': data.get('due_date'),
            'done': data.get('done', False)
        }
        created_task = tasksDAO.create(task)
        return jsonify(created_task), 201

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT', 'DELETE'])
def task_by_id(task_id):
    task = tasksDAO.findByID(task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404

    if request.method == 'GET':
        return jsonify(task)

    elif request.method == 'PUT':
        data = request.get_json()
        if not data:
            abort(400, "Invalid JSON data")
        updated_task = {
            'title': data.get('title'),
            'description': data.get('description'),
            'due_date': data.get('due_date'),
            'done': data.get('done', False)
        }
        tasksDAO.update(task_id, updated_task)
        return jsonify({'message': 'Task updated successfully'})

    elif request.method == 'DELETE':
        tasksDAO.delete(task_id)
        return jsonify({'message': 'Task deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
