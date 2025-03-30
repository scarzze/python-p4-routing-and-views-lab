from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<text>')
def print_text(text):
    print(text)  # Prints to console
    return text    # Returns text in browser

@app.route('/count/<int:num>')
def count(num):
    # Generate numbers from 0 to num-1, then add a final newline
    return '\n'.join(str(i) for i in range(num)) + '\n'

@app.route('/math/<int:num1>/<op>/<int:num2>')
def math(num1, op, num2):
    # Support the operations: +, -, *, div, %
    if op == '+':
        return str(num1 + num2)
    elif op == '-':
        return str(num1 - num2)
    elif op == '*':
        return str(num1 * num2)
    elif op == 'div':
        if num2 == 0:
            return "Cannot divide by zero"
        return str(num1 / num2)
    elif op == '%':
        return str(num1 % num2)
    else:
        return "Invalid operation", 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)
