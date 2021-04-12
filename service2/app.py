from flask import Flask, request
from random import randint
from os import getenv
import requests

app=Flask(__name__)

@app.route('/randint', methods=['GET', 'POST'])
def randintgen():
    randnum = f'{randint(100000, 999999)}'
    return randnum

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5501, debug=True)