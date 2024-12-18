from flask import Flask
import sys
import os

# Add the parent directory to the PYTHONPATH if running locally
if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.routes import routes
app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def index():
    return "Welcome to the FIRE Calculator!"

if __name__ == '__main__':
    app.run(debug=False)