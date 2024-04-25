import os
import s3fs 
import pandas as pd
import googleapiclient.discovery
from googleapiclient.errors import HttpError

def get_youtube_service(api_service_name="youtube", api_version="v3"):
    """ Initialize YouTube API service """
    developer_key = os.getenv("YOUTUBE_DEVELOPER_KEY")
    if not developer_key:
        raise ValueError("Missing environment variable: YOUTUBE_DEVELOPER_KEY")
    return googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)

def process_comments(response_items):
    """ Extract comments and their details from the API response """
    comments_info = []
    for item in response_items:
        # Extracting top-level comment
        comment = item["snippet"]["topLevelComment"]["snippet"]
        comments_info.append({
            "authorDisplayName": comment["authorDisplayName"],
            "textOriginal": comment["textOriginal"],
            "publishedAt": pd.to_datetime(comment["publishedAt"]).strftime('%Y-%m-%d %H:%M:%S')
        })

        # Extracting replies, if present
        if "replies" in item:
            for reply in item["replies"]["comments"]:
                reply_comment = reply["snippet"]
                comments_info.append({
                    "authorDisplayName": reply_comment["authorDisplayName"],
                    "textOriginal": reply_comment["textOriginal"],
                    "publishedAt": pd.to_datetime(reply_comment["publishedAt"]).strftime('%Y-%m-%d %H:%M:%S')
                })
    return comments_info

def fetch_comments(video_id,max_results=200):
    """ Fetch comments for a given video ID """
    comments = []
    try:
        youtube = get_youtube_service()
        request = youtube.commentThreads().list(
            part="id,snippet,replies",
            videoId=video_id,
            maxResults=100
        )
        while request and len(comments) < max_results:
            response = request.execute()
            comments += process_comments(response['items'])
            if len(comments) >= max_results:
                comments = comments[:max_results]  # Trim excess comments if over max_results
            request = youtube.commentThreads().list_next(request, response)

    except HttpError as error:
        print(f"An HTTP error occurred: {error}")
        return []

    return comments


def run_youtube_etl():
    video_id = "q8q3OFFfY6c"
    comments = fetch_comments(video_id,max_results=200)
    if comments:
        comments_df = pd.DataFrame(comments)
        comments_df.to_csv("s3://youtube-comments-raw/Youtube_video_comments.csv", index=False)
        print("Comments have been saved to CSV file.")
    else:
        print("No comments were found or an error occurred.")

# if __name__ == "__main__":
#     main()
