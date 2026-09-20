# **Share of Voice (SoV) AI Agent — Smart Fan Market Analysis**

## **📌 Overview**
This AI-powered agent collects search results from **Google** and **YouTube** for the keyword *“smart fan”* (and related terms), detects brand mentions, calculates engagement & sentiment, and produces a **Share of Voice (SoV)** report.

This tool was built as a targeted, short-term project for **Atomberg's AIML Internship** application, demonstrating:
- API integration (Google & YouTube)
- NLP for brand detection & sentiment
- Market intelligence analysis with engagement scoring

---

## **⚙️ Features**
- **Multi-source search** — Google Search via SerpAPI + YouTube Data API
- **Brand detection** — Matches text against a list of competitors
- **Engagement scoring** — Weighted formula using views, likes, and comments
- **Sentiment analysis** — Uses HuggingFace Transformers
- **CSV output** — Full report of top N search/video results
- **Sample output** — `results_sample.csv` for review without API keys

---

## **📂 Project Structure**
```
├── analysis.py           # NLP scoring: brand detection, sentiment, engagement
├── config_example.py     # Config template for API keys, keywords, brands
├── main.py               # Orchestrator: calls search & analysis modules
├── requirements.txt      # Python dependencies
├── results_sample.csv    # Example output for reviewers
├── search_serpapi.py     # Google search results via SerpAPI
├── search_youtube.py     # YouTube search & video stats
└── README.md             # Project documentation
```

---

## **📊 Workflow Diagram**
```
CONFIG (API keys, keywords, brands)
        ↓
SEARCH MODULES
   Google (SerpAPI)
   YouTube Data API
        ↓
ANALYSIS MODULE
   Brand detection
   Engagement scoring
   Sentiment analysis
        ↓
RESULTS
   CSV file with SoV % per brand
   Summary printed to console
```

---

## **🚀 How to Run**
### 1️⃣ Clone the repo
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API keys
Copy the template:
```bash
cp config_example.py config.py
```
Edit `config.py`:
```python
SERPAPI_KEY = "your-serpapi-key"
YOUTUBE_API_KEY = "your-youtube-api-key"
BRANDS = ["Atomberg", "Havells", "Crompton", "Usha"]
KEYWORDS = ["smart fan", "energy saving fan"]
TOP_N = 30
```

### 4️⃣ Run the agent
```bash
python main.py
```

Output:
- `results.csv` → full data with engagement & sentiment
- Console summary of brand Share of Voice

---

## **📑 Sample Output**
You can view **`results_sample.csv`** for an example output **without** running API calls.  
Example row:
| source | text | views | link | brand | sentiment | engagement | score |
|--------|------|-------|------|-------|-----------|------------|-------|
| google | Atomberg smart fan saves 65% energy... | - | https://... | Atomberg | 0.92 | - | 1.84 |

---

## **💡 Possible Extensions**
- Add Instagram & X (Twitter) scraping
- Advanced sentiment model with aspect-based analysis
- Dashboard visualization with Plotly or Streamlit

---

## **📌 Author's Note**
> This project was scoped and executed in a short timeframe specifically for the Atomberg internship.  
> The commit history is compressed due to the deadline, but every line of code is authored by me and I can walk through the full workflow during the interview.
