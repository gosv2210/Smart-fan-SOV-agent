"""
analysis.py
-----------
Contains brand detection, engagement scoring, and sentiment analysis logic.

Functions:
    detect_brand(text, brands)
        - Checks if any brand names appear in the text

    compute_engagement(stats)
        - Calculates engagement score using views, likes, comments

    sentiment_score(text)
        - Uses HuggingFace Transformers sentiment analysis pipeline

    score_for_result(text, stats, brands, brand)
        - Combines brand mention, engagement, and sentiment to produce a weighted score
"""
import math
from transformers import pipeline
import spacy

# Load once when module imported. May be slow first time.
try:
    nlp_spacy = spacy.load("en_core_web_sm")
except Exception:
    nlp_spacy = None

sentiment = pipeline("sentiment-analysis")

def detect_brand(text, brands):
    text_l = (text or "").lower()
    found = []
    for b in brands:
        if b.lower() in text_l:
            found.append(b)
    return found

def compute_engagement(stats):
    v = stats.get("viewCount", 0)
    l = stats.get("likeCount", 0)
    c = stats.get("commentCount", 0)
    return math.log1p(v) + 2*math.log1p(l) + math.log1p(c)

def sentiment_score(text):
    if not text:
        return 0.5
    res = sentiment(text[:512])
    label = res[0]['label']
    score = res[0]['score']
    if label.lower().startswith("pos"):
        return 0.5 + 0.5*score
    else:
        return 0.5 - 0.5*score

def score_for_result(text, stats, brands, brand):
    mentions = 1 if brand in detect_brand(text, brands) else 0
    eng = compute_engagement(stats)
    sent = sentiment_score(text)
    return mentions * eng * (1 + (sent - 0.5))
