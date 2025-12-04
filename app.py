from flask import Flask, request, jsonify
import json
import random

app = Flask(__name__)


with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)


@app.get("/quote/all")
def all_quotes():
    return jsonify(quotes)


@app.get("/quote/random")
def random_quote():
    return jsonify(random.choice(quotes))


@app.post("/quote/add")
def add_quote():
    new_quote = request.json
    quotes.append(new_quote)

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)
    
    return jsonify({"message": "Citation ajoutée"})


@app.get("/health")
def health():
    return jsonify({"status": "ok", "count": len(quotes)})





app.run(debug=True)
