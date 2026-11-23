from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    # Small change made here to trigger the pipeline
    return {"message": "Application DevOps opérationnelle - Version 2"}

@app.route("/health")
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)