# api/ping.py
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is alive!"

if __name__ == "__main__":
    app.run()
