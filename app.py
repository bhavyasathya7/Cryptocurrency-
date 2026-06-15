from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv("crypto_prices.csv")
    coins = data.to_dict(orient='records')
    return render_template("index.html", coins=coins)

if __name__ == "__main__":
    app.run(debug=True)