# Flask Application

This is a Flask application designed to demonstrate how to set up and run a web server using Flask, a lightweight WSGI web application framework in Python.

## Installation

### Prerequisites

- Make sure you have Python installed (version 3.6 or later).
- Install [pip](https://pip.pypa.io/en/stable/) if it’s not already installed.

### Set Up

1. **Clone the repository** (if applicable):
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. **Create a virtual environment** (recommended):
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install Flask**:
    ```bash
    pip install Flask
    ```

## Running the Application

1. **Set the FLASK_APP environment variable**:
    - On Windows:
        ```bash
        set FLASK_APP=app.py
        ```
    - On macOS/Linux:
        ```bash
        export FLASK_APP=app.py
        ```

2. **Run the Flask application**:
    ```bash
    flask run
    ```

3. **Access the application**: Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

You can modify the `app.py` file to add routes and handle requests. For example:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
