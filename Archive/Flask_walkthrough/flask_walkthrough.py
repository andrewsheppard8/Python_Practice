from flask import Flask, render_template
import requests

app = Flask(__name__)

# #when someone hits main url, return message
# @app.route("/")
# def index():
#     return "Drink more coffee"

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000, debug=True)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None, None  # API failed
    
    data = response.json()
    meme_large = data["url"]   # direct meme image
    subreddit = data["subreddit"]
    return meme_large, subreddit

@app.route("/")
def index():
    meme_pic, subreddit = get_meme()
    if meme_pic is None:
        return "Could not load meme. Try again later!"
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)