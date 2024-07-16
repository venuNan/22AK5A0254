import requests
from flask import Flask,jsonify


app = Flask(__name__)

prev_window = []
cur_window = []

@app.route("/")
def home():
    return ""



@app.route("/numbers/e")
def even():
    response = requests.get("http://20.244.56.144/test/even").json()

    numbers = response["numbers"]
    sum = 0
    prev_window = cur_window
    for i in numbers:
        avg += i
    
    avg = sum/len(numbers)

    for i in numbers:
        if i not in prev_window:
            cur_window.append(i)

    return jsonify({
        "numbers":numbers,
        "windowPrevState":prev_window,
        "windowCurrState":cur_window,
        "avg":avg
    })

@app.route("/numbers/p")
def even():
    response = requests.get("http://20.244.56.144/test/primes").json()

    numbers = response["numbers"]
    sum = 0
    prev_window = cur_window
    for i in numbers:
        avg += i
    
    avg = sum/len(numbers)

    for i in numbers:
        if i not in prev_window:
            cur_window.append(i)

    return jsonify({
        "numbers":numbers,
        "windowPrevState":prev_window,
        "windowCurrState":cur_window,
        "avg":avg
    })


@app.route("/numbers/f")
def even():
    response = requests.get("http://20.244.56.144/test/fibo").json()

    numbers = response["numbers"]
    sum = 0
    prev_window = cur_window
    for i in numbers:
        avg += i
    
    avg = sum/len(numbers)

    for i in numbers:
        if i not in prev_window:
            cur_window.append(i)

    return jsonify({
        "numbers":numbers,
        "windowPrevState":prev_window,
        "windowCurrState":cur_window,
        "avg":avg
    })


@app.route("/numbers/r")
def even():
    response = requests.get("http://20.244.56.144/test/rand").json()

    numbers = response["numbers"]
    sum = 0
    prev_window = cur_window
    for i in numbers:
        avg += i
    
    avg = sum/len(numbers)

    for i in numbers:
        if i not in prev_window:
            cur_window.append(i)

    return jsonify({
        "numbers":numbers,
        "windowPrevState":prev_window,
        "windowCurrState":cur_window,
        "avg":avg
    })

    
if __name__ == "__main__":
    app.run(port=9876)


