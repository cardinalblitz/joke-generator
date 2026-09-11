"""Flask web app for the joke generator."""

from flask import Flask, render_template, jsonify, request
from joke_generator import JokeGenerator

app = Flask(__name__)
generator = JokeGenerator()

@app.route("/")
def index():
    """Render the home page."""
    return render_template("index.html")

@app.route("/api/joke")
def get_joke():
    """API endpoint to get a random joke."""
    category = request.args.get("category", "Any")
    safe_mode = request.args.get("safe_mode", "false").lower() == "true"
    
    joke_data = generator.get_random_joke(category, safe_mode)
    
    if joke_data and not joke_data.get("error"):
        return jsonify({
            "success": True,
            "joke": generator.format_joke(joke_data),
            "category": joke_data.get("category"),
            "type": joke_data.get("type")
        })
    
    return jsonify({
        "success": False,
        "error": "Failed to fetch joke"
    }), 400

@app.route("/api/categories")
def get_categories():
    """API endpoint to get available joke categories."""
    categories = ["Any", "General", "Knock-Knock", "Programming", "Dark", "Pun"]
    return jsonify(categories)

if __name__ == "__main__":
    app.run(debug=True)
