from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Application DevOps opérationnelle"}

@app.route("/health")
def health():
    return {"status": "ERROR"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)






       