from flask import Flask, Response, request, jsonify
import requests
import random
app=Flask(__name__)

@app.route('/complete', methods=['GET','POST'])
def complete_result():
    randalpha = str(requests.get("http://service3:5502/randalpha"))

    alphacheck = ('a', 'b', 'c')
    complete = ""
    rand = random.randint(1, 9)
    if randalpha.startswith(alphacheck):
        complete = f'{rand * 10}'

    else:
        complete = f'{rand}'

    
    return complete

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5503, debug=True)