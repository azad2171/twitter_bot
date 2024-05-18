from auth import get_twitter_conn_v1, get_twitter_conn_v2

def post_to_twitter(tweet_text, file_paths = []):
    client_v1 = get_twitter_conn_v1()
    client_v2 = get_twitter_conn_v2()

    media_ids = []
    for file_path in file_paths:
        media = client_v1.media_upload(filename=file_path)
        media_ids.append(media.media_id)
    
    media_ids = media_ids if media_ids else None

    client_v2.create_tweet(text=tweet_text, media_ids=media_ids)