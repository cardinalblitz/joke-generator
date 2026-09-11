# 🎭 Random Joke Generator

A fun and interactive joke generator application that fetches random jokes from the [JokeAPI](https://jokeapi.dev/). This project includes both a command-line interface and a web application.

## Features

✨ **Multiple Joke Categories**
- Any
- General
- Knock-Knock
- Programming
- Dark
- Pun

🛡️ **Safe Mode** - Filter out offensive jokes

💻 **Multiple Interfaces**
- Command-line interface (Python)
- Web application (Flask)
- REST API endpoints

⚡ **Fast & Reliable** - Uses the free JokeAPI

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup

1. Clone the repository:
```bash
git clone https://github.com/cardinalblitz/joke-generator.git
cd joke-generator
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

For web app support, also install Flask:
```bash
pip install flask
```

## Usage

### Command Line

Run the basic joke generator:
```bash
python joke_generator.py
```

### Web Application

Start the Flask web server:
```bash
python web_app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

### API Endpoints

When running the web app, you can access these API endpoints:

#### Get a Random Joke
```
GET /api/joke?category=Programming&safe_mode=false
```

Parameters:
- `category` (optional): Joke category (default: "Any")
- `safe_mode` (optional): Filter offensive jokes (default: false)

Example Response:
```json
{
  "success": true,
  "joke": "Why do programmers prefer dark mode? Because light attracts bugs!",
  "category": "Programming",
  "type": "single"
}
```

#### Get Available Categories
```
GET /api/categories
```

Example Response:
```json
[
  "Any",
  "General",
  "Knock-Knock",
  "Programming",
  "Dark",
  "Pun"
]
```

## Code Structure

```
joke-generator/
├── joke_generator.py      # Core joke generator class
├── config.py             # Configuration settings
├── web_app.py            # Flask web application
├── templates/
│   └── index.html        # Web interface
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Class: JokeGenerator

### Methods

#### `get_random_joke(category: str = "Any", safe_mode: bool = False) -> Dict`
Fetch a random joke from the JokeAPI.

#### `format_joke(joke_data: Dict) -> str`
Format joke data into a readable string.

#### `get_and_print_joke(category: str = "Any", safe_mode: bool = False) -> None`
Fetch and print a random joke.

#### `get_multiple_jokes(count: int = 5, category: str = "Any", safe_mode: bool = False) -> list`
Fetch multiple jokes.

## Example Usage

```python
from joke_generator import JokeGenerator

# Create an instance
generator = JokeGenerator()

# Get and print a random programming joke
generator.get_and_print_joke(category="Programming")

# Get multiple jokes
jokesList = generator.get_multiple_jokes(count=5, safe_mode=True)

# Get raw joke data
raw_joke = generator.get_random_joke(category="Dark")
formatted = generator.format_joke(raw_joke)
print(formatted)
```

## API Source

This project uses the free [JokeAPI](https://jokeapi.dev/) by Sv443.

**API URL:** `https://v2.jokeapi.dev/joke`

## License

MIT License - Feel free to use this project for personal or commercial purposes.

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub.

---

**Made with ❤️ by cardinalblitz**
