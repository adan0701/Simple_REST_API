from flask import Flask, request, jsonify, abort
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
    allowed_keys = {"text", "author"}
    new_quote = request.json
    if not new_quote or "text" not in new_quote or "author" not in new_quote or not new_quote["text"] or not new_quote["author"]:
        abort(400)
    for key in new_quote:
        if key not in allowed_keys:
            abort(400)
    
    quotes.append(new_quote)

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(quotes, f, indent=4, ensure_ascii=False)
    
    return jsonify({"message": "Citation ajoutée"})


@app.get("/health")
def health():
    return jsonify({"status": "ok", "count": len(quotes)})



@app.errorhandler(400)
def bad_request(obj):
    return jsonify({"error": "Bad request (400)"})

@app.errorhandler(401)
def unauthorized(obj):
    return jsonify({"error": "Unauthorized (401)"})

@app.errorhandler(403)
def forbidden(obj):
    return jsonify({"error": "Forbidden (403)"})

@app.errorhandler(404)
def not_found_handler(obj):
    return jsonify({"error": "Route not found (404)"})

@app.errorhandler(405)
def method_not_allowed(obj):
    return jsonify({"error": "Method not allowed (405)"})

@app.errorhandler(409)
def conflict(obj):
    return jsonify({"error": "Conflict (409)"})

@app.errorhandler(500)
def server_error(obj):
    return jsonify({"error": "Server error (500)"})


app.run(debug=True)
