from flask import Flask, request, Response
import random
import string

app=Flask(__name__)

@app.route('/randalpha', methods=['GET'])
def randalphagen():
    loweralpha = string.ascii_lowercase
    upperalpha = string.ascii_uppercase
    randomalpha = random.choice(loweralpha)
    return randomalpha

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5502, debug=True)