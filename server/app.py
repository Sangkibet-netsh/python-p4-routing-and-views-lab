#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'


@app.route('/print/<string:parameter>')
def printer(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<string:num>')
def count(num):
    # str = ""
    decremented_arr = [str(number) for number in range(int(num))]
    decremented_arr.sort()
    result_str = "\n".join(decremented_arr) + "\n"
    return result_str

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, operation, num2):
    if(operation == "+"):
        return str(num1 + num2)
    elif(operation == "-"):
        return str(num1-num2)
    elif(operation == '*'):
        return str(num1*num2)
    elif(operation == 'div'):
        return str(num1/num2)
    else:
        return str(num1 % num2)











