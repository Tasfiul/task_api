from flask import Flask, jsonify, abort, request

from . import app

# Sample data - in-memory list of tasks
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

next_task_id = 3    

@app.route('/')
def index():
    return "Task API is running!"

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Return the list of tasks as a JSON response
    return jsonify({'tasks': tasks})

#  Route to get a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id): # Flask passes the task_id from the URL here
    # Find the task with the matching ID
    task = [task for task in tasks if task['id'] == task_id]

    # If no task was found with that ID, return a 404 Not Found error
    if len(task) == 0:
        abort(404) # We use abort to return standard HTTP errors

    # If the task was found, return the first matching task as JSON
    return jsonify({'task': task[0]})

#  Route to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Check if the request body is JSON and has a 'title' field
    if not request.json or not 'title' in request.json:
        # If not, return a 400 Bad Request error
        abort(400)

    # Create the new task dictionary
    global next_task_id # Declare that we want to modify the global variable
    task = {
        'id': next_task_id,
        'title': request.json['title'],
        'description': request.json.get('description', ""), # Get description if provided, otherwise empty string
        'done': False
    }
    next_task_id += 1 # Increment the counter for the next task

    # Add the new task to our list
    tasks.append(task)

    # Return the newly created task with a 201 Created status code
    return jsonify({'task': task}), 201 # Return the JSON and the status code

#  Route to update a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    # Find the task first (same logic as get_task)
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404) # Return 404 if task not found

    # Get the incoming updated data
    if not request.json:
        abort(400) # Return 400 if no JSON body

    # Update the task fields if they are present in the request JSON
    if 'title' in request.json:
        task[0]['title'] = request.json['title']
    if 'description' in request.json:
        task[0]['description'] = request.json['description']
    if 'done' in request.json:
        # Check if 'done' is a boolean, return 400 if not
        if type(request.json['done']) is not bool:
             abort(400)
        task[0]['done'] = request.json['done']

    # Return the updated task
    return jsonify({'task': task[0]})

# Route to delete a specific task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # Find the task first (same logic as get/put)
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404) # Return 404 if task not found

    # Remove the task from the list
    # We need to remove the specific dictionary object found
    tasks.remove(task[0])

    # Return a success response
    # A common practice is to return an empty success response or status 200
    return jsonify({'result': True}) # Or simply return '', 204 (No Content)


if __name__ == '__main__':
    app.run(debug=True)