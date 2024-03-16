from flask import Flask, request, g
import praw
import time
import logging as log
from openai import OpenAI
import webbrowser
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handleGet():
    return

if __name__ == '__main__':
    reddit = praw.Reddit(client_id = os.getenv('REDDIT_CLIENT_ID'),
            client_secret = os.getenv('REDDIT_CLIENT_SECRET'),
            user_agent = os.getenv('REDDIT_USER_AGENT'))

    print(reddit.read_only)

    subreddit = reddit.subreddit('wallstreetbets')  # Change 'python' to the desired subreddit name
    print(subreddit)
    stream = subreddit.stream.submissions()
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),
    )

    # Continuously process live posts
    for post in stream:
        try:
            # print(post.title)  # Print post title
            # print(post.author)  # Print post author
            # print(post.created_utc)  # Print post creation time
            # print(post.selftext)  # Print post content (if it's a text post)
            
            if post.selftext.strip():  # Check if post.selftext is not empty

                print(  "***")
                print(post.selftext)
                print(  "***")

                summary = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": f'''Visualize a humorous juxtaposition where a character or object representing the central theme of '{post.selftext}' is placed in a fintech-related scenario, highlighting the amusing contrast or unexpected integration between the two worlds. The scene should include subtle fintech elements like digital charts, cryptocurrency symbols, or e-wallets, and portray the character or object in a comical light, attempting to navigate or make sense of these modern financial tools and trends.{post.selftext}''',
                        }
                    ],
                    model="gpt-3.5-turbo",
                )

                if summary.choices and hasattr(summary.choices[0], 'message') and hasattr(summary.choices[0].message, 'content'):
                    print(summary.choices[0].message.content)
                    imgPrompt=summary.choices[0].message.content
                    # call dalle to generate an image
                    response = client.images.generate(
                        model="dall-e-3",
                        prompt=imgPrompt,
                        size="1024x1024",
                        quality="standard",
                        n=1,
                    )

                    # Show the result that has been pushed to an url
                    webbrowser.open(response.data[0].url)
                else:
                    print("No content available.")
            else:
                print("Post has no text.")
            print('-------------------------------------------------------')
        except Exception as e:
            print(f"An error occurred: {e}")
            # Sleep for some time before retrying
            time.sleep(60)  # Sleep for 60 seconds before retrying
    
    # log.info("Starting flask server")
    # app.run(port=5000, debug=True)  # Run the Flask app