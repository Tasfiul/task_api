# task_api
A simple RESTful task-api that handles CRUD operation.
## Features

* Create new tasks
* Retrieve a list of all tasks
* Retrieve a specific task by ID
* Update an existing task
* Delete a task

## Technologies Used

* Python
* Flask
* `jsonify` (Flask)
* `request` (Flask)
## Setup and Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Tasfiul/task_api
    ```
2.  Navigate to the project directory:
    ```bash
    cd task_api
    ```
3.  Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
## How to Run

1.  Make sure your virtual environment is activated.
2.  Set the `FLASK_APP` environment variable to point to your application instance (assuming your Flask app instance is named `app` in `your_main_app_file.py` within a package):
    ```powershell
    # On Windows (PowerShell)
    $env:FLASK_APP = "hello_app.webapp:app"
3.  Run the Flask application:
    ```bash
    flask run
    ```
## API Endpoints

The API base URL is `http://127.0.0.1:5000/`.

* **GET /tasks**
    * Method: `GET`
    * Description: Retrieves a list of all tasks.
    * Response: JSON array of task objects.

* **GET /tasks/<int:task_id>**
    * Method: `GET`
    * Description: Retrieves a specific task by its ID.
    * Response: JSON object for the task if found, or an error message.

* **POST /tasks**
    * Method: `POST`
    * Description: Creates a new task.
    * Request Body: JSON object containing task details (e.g., `{"title": "New Task", "description": "Details"}`).
    * Response: JSON object for the newly created task.

* **PUT /tasks/<int:task_id>**
    * Method: `PUT`
    * Description: Updates an existing task by its ID.
    * Request Body: JSON object with updated task details.
    * Response: JSON object for the updated task.

* **DELETE /tasks/<int:task_id>**
    * Method: `DELETE`
    * Description: Deletes a specific task by its ID.
    * Response: Success or error message.
