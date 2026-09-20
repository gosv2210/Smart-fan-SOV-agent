"""
search_youtube.py
-----------------
Fetches YouTube search results and video statistics.

Functions:
    youtube_search(query, api_key, max_results=25)
        - Searches YouTube videos for the given keyword
        - Returns list of dicts with video metadata

    get_video_stats(video_id, api_key)
        - Retrieves view count, like count, and comment count for a video

Dependencies:
    - google-api-python-client (pip install google-api-python-client)
    - YouTube Data API key required (store in config.py as YOUTUBE_API_KEY)
"""
from googleapiclient.discovery import build

def youtube_search(query, api_key, max_results=25):
    youtube = build('youtube', 'v3', developerKey=api_key)
    response = youtube.search().list(
        q=query, part='snippet', type='video', maxResults=max_results
    ).execute()
    hits = []
    for item in response.get('items', []):
        vid = item['id'].get('videoId')
        snippet = item['snippet']
        hits.append({
            "source": "youtube",
            "videoId": vid,
            "title": snippet.get('title'),
            "description": snippet.get('description'),
            "channelTitle": snippet.get('channelTitle')
        })
    return hits

def get_video_stats(video_id, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)
    res = youtube.videos().list(part='statistics', id=video_id).execute()
    items = res.get('items', [])
    if not items: return {}
    stats = items[0].get('statistics', {})
    return {
        "viewCount": int(stats.get('viewCount', 0)),
        "likeCount": int(stats.get('likeCount', 0)) if 'likeCount' in stats else 0,
        "commentCount": int(stats.get('commentCount', 0)) if 'commentCount' in stats else 0
    }
