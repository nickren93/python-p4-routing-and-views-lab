#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = [str(num) for num in range(parameter)]
    return '\n'.join(numbers) + '\n'

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    num1 = int(num1)
    num2 = int(num2)

    if str(operation) == "+":
        result = num1 + num2
    elif str(operation) == "-":
        result = num1 - num2
    elif str(operation) == "*":
        result = num1 * num2
    elif str(operation) == "div":
        result = num1 / num2
    elif str(operation) == "%":
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
