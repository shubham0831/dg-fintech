# dg-fintech

## Project Setup

This project is a Python application that uses the Reddit API to stream posts from a subreddit, uses OpenAI to generate a summary and an image based on the post, and then opens the generated image in a web browser.

### Prerequisites

- Python 3.6 or higher
- [PRAW](https://praw.readthedocs.io/en/latest/getting_started/installation.html) (Python Reddit API Wrapper)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)
- [OpenAI Python](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_install_the_OpenAI_API_python_client.md)

### Environment Variables

You need to set the following environment variables:

- `REDDIT_CLIENT_ID`: Your Reddit application's client ID
- `REDDIT_CLIENT_SECRET`: Your Reddit application's client secret
- `REDDIT_USER_AGENT`: A unique user agent for your Reddit application
- `OPENAI_API_KEY`: Your OpenAI API key

You can set these variables in your shell, or you can use a `.env` file and load it using a library like `python-dotenv`.

### Running the Application

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies with `pip install -r requirements.txt`.
3. Run the application with `python main.py`.

The application will start streaming posts from the 'wallstreetbets' subreddit. For each post, it will generate a summary and an image, and open the image in a web browser.

Note: The Flask server is currently commented out in the `main.py` file. If you want to use it, uncomment the last two lines of the file and visit `localhost:5000` in your web browser after starting the application.


![img-qDhXFBwj5qqn1vWwhbdV50cQ](https://github.com/shubham0831/dg-fintech/assets/10244040/8794051b-795a-4fb9-87a0-1ec80c5c161f)
