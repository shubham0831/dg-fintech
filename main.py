from flask import Flask, request, g
import praw
import time
import logging as log

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handleGet():
    return

if __name__ == '__main__':
    reddit = praw.Reddit(client_id ='',
                     client_secret ='',
                     user_agent ='dg-stream')

    print(reddit.read_only)

    subreddit = reddit.subreddit('wallstreetbets')  # Change 'python' to the desired subreddit name
    print(subreddit)
    stream = subreddit.stream.submissions()

    # Continuously process live posts
    for post in stream:
        try:
            # print(post.title)  # Print post title
            # print(post.author)  # Print post author
            # print(post.created_utc)  # Print post creation time
            print(post.selftext)  # Print post content (if it's a text post)
            print('-------------------------------------------------------')
        except Exception as e:
            print(f"An error occurred: {e}")
            # Sleep for some time before retrying
            time.sleep(60)  # Sleep for 60 seconds before retrying
    
    # log.info("Starting flask server")
    # app.run(port=5000, debug=True)  # Run the Flask app