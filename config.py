"""Configuration for the joke generator."""

# Available joke categories
JOKE_CATEGORIES = [
    "Any",
    "General",
    "Knock-Knock",
    "Programming",
    "Dark",
    "Pun"
]

# Default settings
DEFAULT_CATEGORY = "Any"
DEFAULT_SAFE_MODE = False
DEFAULT_TIMEOUT = 5

# API Configuration
JOKE_API_URL = "https://v2.jokeapi.dev/joke"
