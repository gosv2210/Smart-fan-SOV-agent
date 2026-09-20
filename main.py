"""
main.py
--------
This is the script for the Share-of-Voice (SoV) AI Agent.

What it does:
1. Reads keywords and brand list from config.py
2. Fetches search results from Google (via SerpAPI) and YouTube (via YouTube Data API)
3. Runs brand detection, engagement scoring, and sentiment analysis
4. Calculates Share of Voice percentages for each brand
5. Saves the top results to results.csv and prints summary in console

Run:
    python main.py
Output:
    results.csv  - CSV file containing top N search results with brand mentions
"""
import config
import pandas as pd
from search_serpapi import serp_search
from search_youtube import youtube_search, get_video_stats
from analysis import score_for_result

def analyze_keyword(keyword):
    results = []
    # Google
    try:
        g = serp_search(keyword, config.SERPAPI_KEY, num=config.TOP_N)
        for r in g:
            text = (r.get("title","") + " " + r.get("snippet","")).strip()
            stats = {"viewCount":0,"likeCount":0,"commentCount":0}
            results.append((r["source"], text, stats, r.get("link")))
    except Exception as e:
        print('SerpAPI error or not configured:', e)

    # YouTube
    try:
        y = youtube_search(keyword, config.YOUTUBE_API_KEY, max_results=config.TOP_N)
        for v in y:
            stats = get_video_stats(v.get("videoId"), config.YOUTUBE_API_KEY) if v.get("videoId") else {}
            text = (v.get("title","") + " " + v.get("description","")).strip()
            results.append((v["source"], text, stats, f"https://youtu.be/{v.get('videoId')}"))
    except Exception as e:
        print('YouTube API error or not configured:', e)

    return results

def compute_sov(results):
    brands = config.BRANDS
    brand_scores = {b:0.0 for b in brands}

    for src, text, stats, link in results:
        for b in brands:
            brand_scores[b] += score_for_result(text, stats, brands, b)

    total = sum(brand_scores.values()) or 1.0
    sov = {b: (brand_scores[b]/total)*100 for b in brands}
    return sov, brand_scores

if __name__ == '__main__':
    all_results = []
    for kw in config.KEYWORDS:
        print('Analyzing keyword:', kw)
        all_results.extend(analyze_keyword(kw))

    sov, raw_scores = compute_sov(all_results)
    print("Share of Voice (percent):\n", sov)
    df = pd.DataFrame([
        {"source": r[0], "text": r[1][:200], "views": r[2].get('viewCount',0), "link": r[3]}
        for r in all_results
    ])
    df.to_csv("results.csv", index=False)
    print("Saved results.csv with top hits.")
