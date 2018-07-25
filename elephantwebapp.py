from flask import Flask, render_template, request
import tweepy

# This is create instance of Flask. app is variable
app = Flask("MyApp")

# Default route his method will be called when you hit http://127.0.0.0:5000/
@app.route("/")
def home():
    return render_template(
        "elephant.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter

@app.route("/african")
def african():
    return render_template(
        "african.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter

@app.route("/asian")
def asian():
    return render_template(
        "asian.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter

@app.route("/conservation")
def conservation():
    return render_template(
        "conservation.html")  # render_template method is a special function flask which redirect to the html file mentioned in the paramter





@app.route("/contact")
def twitter():
    auth = tweepy.OAuthHandler("YtJaHzQh75TLJ2XacgH28T6vU","MD0FlKnHQ95UCNpkRWW0xfz5BtwEV8ocjckHS0Lx2BkwIYHpjb")
    auth.set_access_token ("33679048-GhUnRhh1biI7bX4Dq1bdT4IJrSAxCfMX8vlRBXQWB", "BJPaAMNeAtyxHBkARbDiFKgjRnB4hByy664OBRNoiTnrl")
    twitter_api = tweepy.API(auth)
    cfg_tweets = twitter_api.search(
    q = "ElephantConservation" #Twitter handle you want to search by
    )
    # for tweet in cfg_tweets:
    # print tweet.user.name + ":" + tweet.text + "\n"

    return render_template(
        "contact.html",elly_tweets = cfg_tweets)  # render_template method is a special function flask which redirect to the html file mentioned in the paramter



if __name__ == "__main__":
    app.run(debug=True)
