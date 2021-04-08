from flask import Flask, Response, request, jsonify
import requests

app=Flask(__name__)

@app.route('/complete')
def complete_result():
    service2_response = requests.get("http://service2:5501/randint")
    service3_response = requests.get("http://service3:5502/randalpha")

    alphacheck = ('a', 'b', 'c')

    if randomalpha.startswith(alphacheck):
        result = int(randint) * 10 

    else:
        result = int(randint)

    packet = {
        "randomalpha": randomalpha, "randint": randint, "result": result
    }

    return jsonify(packet)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5503, debug=True)