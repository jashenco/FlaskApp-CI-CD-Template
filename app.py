from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>CD testttttt.... Hello, World! Updated. Added CI pipeline. Let's get started on the CD. Oh wait... CD already done. Test 2.</p>"

if __name__ == "__main__": 
    app.run(debug=True, host='0.0.0.0')