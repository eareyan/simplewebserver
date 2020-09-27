from flask import Flask
from flask import jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello():
    """ Simple hello worlds """
    return 'Hi!!, Hello World!'

@app.route('/data')
def show_data():
    df = pd.read_csv("https://raw.githubusercontent.com/noahgift/sugar/master/data/education_sugar_cdc_2003.csv")
    return jsonify(df.to_dict())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)