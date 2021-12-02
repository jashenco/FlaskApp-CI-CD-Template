from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! Updated. Added CI pipeline. Let's get started on the CD.</p>"

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')