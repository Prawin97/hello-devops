from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 Hello DevOps v2</h1>
    <h2>Version 2</h2>
    <p>Welcome to my CI/CD Pipeline</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)