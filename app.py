from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Automation is the key to scale.",
    "Infrastructure as Code is the way.",
    "Ship early, ship often.",
    "DevOps is a culture, not just a role.",
    "If it's not in Git, it doesn't exist."
]

@app.route('/')
def get_quote():
    return jsonify({"quote": random.choice(quotes), "status": "running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)