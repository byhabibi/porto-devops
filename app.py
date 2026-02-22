from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>DevOps Engineer Portfolio</h1>
    <p>Server running with Docker & Nginx reverse proxy</p>
    <p>Auto deployed from GitHub</p>
    <p> ======================================</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
