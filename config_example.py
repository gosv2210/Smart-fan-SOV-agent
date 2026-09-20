"""
config_example.py
-----------------
Configuration template for the SoV AI Agent.

Copy this file to config.py and add your API keys:
    SERPAPI_KEY = "YOUR_SERPAPI_KEY"
    YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

Also configure:
    TOP_N      - number of results to fetch per keyword
    BRANDS     - list of brands to track
    KEYWORDS   - search keywords

IMPORTANT: Never commit config.py with real keys to a public repo.
"""

# Your SerpAPI key for Google search
SERPAPI_KEY = "YOUR_SERPAPI_KEY"

# Your YouTube Data API key
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"

# Number of top results to fetch for each keyword
TOP_N = 30

# List of brand names to track in search results
BRANDS = ["Atomberg", "Havells", "Crompton", "Usha"]

# Keywords to search
KEYWORDS = ["smart fan", "energy saving fan"]
