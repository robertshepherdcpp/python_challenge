from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask App!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return str(a + b)

# Add a new route /subtract/<int:a>/<int:b> that returns the difference of two numbers.
# Add a route /multiply/<int:a>/<int:b> that returns the product of two numbers.
@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return str(a - b)

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return str(a * b)


if __name__ == '__main__':
    app.run(debug=True)