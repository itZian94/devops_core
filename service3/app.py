from flask import Flask, request, Response
import random
import string

app=Flask(__name__)

@app.route('/randalpha', methods=['GET', 'POST'])
def randalphagen():
    loweralpha = ''.join(random.sample(string.ascii_lowercase, 3))
    upperalpha = ''.join(random.sample(string.ascii_uppercase, 2))
    randomalpha = loweralpha
    return randomalpha

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5502, debug=True)