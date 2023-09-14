from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route("/<int:num1>/<int:num2>", methods=['POST', 'GET'])
def lcm(num1,num2):
    if num2 == 0:
        return "Cannot find LCM of zero."
    max_var = max(num1,num2)
    min_var = min(num1,num2)
    temp = max_var
    while(True):
        if(temp%min_var == 0):
            return str(temp)
        temp += max_var
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
