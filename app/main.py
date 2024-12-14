from flask import Flask
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def index():
    return "Welcome to the FIRE Calculator!"

if __name__ == '__main__':
    app.run(debug=True)