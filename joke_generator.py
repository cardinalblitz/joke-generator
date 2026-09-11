import requests
import json
from typing import Dict, Optional

class JokeGenerator:
    """A random joke generator using the JokeAPI."""
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    def __init__(self):
        self.session = requests.Session()
    
    def get_random_joke(self, category: str = "Any", safe_mode: bool = False) -> Optional[Dict]:
        """
        Fetch a random joke from the JokeAPI.
        
        Args:
            category: Joke category - "Any", "General", "Knock-Knock", "Programming", "Dark", "Pun"
            safe_mode: If True, filters out offensive jokes
        
        Returns:
            Dictionary containing joke data or None if request fails
        """
        try:
            # Build query parameters
            params = {}
            if safe_mode:
                params["safe-mode"] = True
            
            # Make the API request
            url = f"{self.BASE_URL}/{category}"
            response = self.session.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching joke: {e}")
            return None
    
    def format_joke(self, joke_data: Dict) -> str:
        """
        Format joke data into a readable string.
        
        Args:
            joke_data: Dictionary returned from the API
        
        Returns:
            Formatted joke string
        """
        if not joke_data or joke_data.get("error"):
            return "Failed to load joke"
        
        if joke_data.get("type") == "single":
            return joke_data.get("joke", "No joke found")
        
        elif joke_data.get("type") == "twopart":
            setup = joke_data.get("setup", "")
            delivery = joke_data.get("delivery", "")
            return f"{setup}\n{delivery}"
        
        return "Unknown joke format"
    
    def get_and_print_joke(self, category: str = "Any", safe_mode: bool = False) -> None:
        """
        Fetch and print a random joke.
        
        Args:
            category: Joke category
            safe_mode: Filter offensive jokes
        """
        joke_data = self.get_random_joke(category, safe_mode)
        formatted_joke = self.format_joke(joke_data)
        print(f"\n{'='*50}")
        print(f"Category: {joke_data.get('category', 'N/A')}")
        print(f"{'='*50}")
        print(formatted_joke)
        print(f"{'='*50}\n")
    
    def get_multiple_jokes(self, count: int = 5, category: str = "Any", safe_mode: bool = False) -> list:
        """
        Fetch multiple jokes.
        
        Args:
            count: Number of jokes to fetch
            category: Joke category
            safe_mode: Filter offensive jokes
        
        Returns:
            List of formatted jokes
        """
        jokes = []
        for _ in range(count):
            joke_data = self.get_random_joke(category, safe_mode)
            formatted = self.format_joke(joke_data)
            jokes.append(formatted)
        return jokes


if __name__ == "__main__":
    generator = JokeGenerator()
    
    print("\n🎭 Random Joke Generator using JokeAPI\n")
    
    # Get a random joke from any category
    print("Getting a random joke...")
    generator.get_and_print_joke()
    
    # Get a programming joke
    print("Getting a programming joke...")
    generator.get_and_print_joke(category="Programming")
    
    # Get multiple jokes
    print("Getting 3 random jokes...")
    multiple_jokes = generator.get_multiple_jokes(count=3)
    for i, joke in enumerate(multiple_jokes, 1):
        print(f"\nJoke {i}:\n{joke}")
