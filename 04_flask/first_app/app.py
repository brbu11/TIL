import random 

from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')

def index():
    return "Hi!"


@app.route('/ssafy')

def ssafy():
    return "Ssafy"

@app.route("/hi/<string:name>")
def hi(name):
    return (f'Hi!! {name}')

@app.route("/pick_lotto")

def pick_lotto():
    numbers = random.sample(range(1,46),6)
    return jsonify(numbers)
@app.route("/dictionary/<string:word>")
def dictionary(word):
    my_dict = {
        "apple" : "사과",
        "orange" : "오렌지",
        "grape" : "포도",
        "melon" : "멜론"
    }
    if word not in my_dict:
        return f"{word}은(는) 없다"
    else:
        return f"{word}은(는) {my_dict[word]}"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
