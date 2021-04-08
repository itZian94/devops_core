from flask import Flask, request, Response
import random

app=Flask(__name__)

@app.route('/randint', methods=['GET'])
def randintgen():
    return f'{random.randint(1,6)}'


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5501, debug=True)