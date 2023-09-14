from flask import Flask, render_template, request, flash, redirect, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route('/', methods=['POST', 'GET'])
def index():
    try :
        num1 = int(request.form.get("first"))
        num2 = int(request.form.get('second'))
        operation = request.form.get('operation')
    except : 
        num1 : 0
        num2 : 0
        operation = 'null'
    else:
        result = 0
        if operation == 'add':
            result = requests.get("http://addition:5050/"+str(num1)+"/"+str(num2)).text
        elif operation == 'minus':
            result = requests.get("http://subtraction:5050/"+str(num1)+"/"+str(num2)).text
        elif operation == 'multiply':
            result = requests.get("http://multiplication:5050/"+str(num1)+"/"+str(num2)).text
        elif operation == 'divide':
            result = requests.get("http://division:5050/"+str(num1)+"/"+str(num2)).text
        elif operation == 'lcm':
            result = requests.get("http://lcm:5050/"+str(num1)+"/"+str(num2)).text
        flash(f'The result of operation {operation} on {num1} and {num2} is {result}')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )

