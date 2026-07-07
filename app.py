from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello Praveen!</h1>
    <h2>Welcome to DBS</h2>
    <p>CI/CD Pipeline v22</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)