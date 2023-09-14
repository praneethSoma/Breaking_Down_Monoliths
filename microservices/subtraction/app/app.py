from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

@app.route("/<int:num1>/<int:num2>", methods=['POST', 'GET'])
def subtract(num1,num2):
    return str(float(num1)-float(num2))
if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
