from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = "eab2e8a00dff672255527a4f550598fb5809627eecff6e15a53dc0447de9d741"

@app.route("/")
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)