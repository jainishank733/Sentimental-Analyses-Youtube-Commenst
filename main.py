from collections import Counter
import youtubecomments as ytc
from wordcloud import wordcloud

googleapikey="AIzaSyAwXKPmjC4WUBknPhLLWezOYoOaowYdujI"



inp = input("Please Enter Video ID: ")
videoid = inp

outputformat = "dataframe"

data = ytc.get_comments(googleapikey, videoid, outputformat)

cs = input("wohoo you did it enter the Filename: ")

data.to_csv(cs,index = False)

import pandas as pd
df = pd.read_csv(cs)
import matplotlib.pyplot as plt
title_words = list(df["textDisplay"].apply(lambda x: x.split()))
title_words = [x for y in title_words for x in y]
print(Counter(title_words).most_common(25))
wc = wordcloud.WordCloud(width=1200, height=500,
                         collocations=False, background_color="white",
                         colormap="tab20b").generate(" ".join(title_words))
plt.figure(figsize=(15,10))
plt.imshow(wc, interpolation="bilinear")
_ = plt.axis("off")
plt.show()

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is: ", sentiment_dict)
    print("sentences was rated as ", sentiment_dict['neg'] * 100, "% Negative")
    print("sentences was rated as ", sentiment_dict['neu'] * 100, "% Neutral")
    print("sentences was rated as ", sentiment_dict['pos'] * 100, "% Positive")

    print("Sentence Overall rated as", end=" ")

    if sentiment_dict['compound'] >= 0.05:
        print("Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print("Negative")
    else:
        print("Neutral")


if __name__ == "__main__":
    import pandas as pd
    dataset = pd.read_csv(cs)
    print(dataset.head())
    print(len(dataset))
    feature_names = ['textDisplay']
    X = dataset[feature_names]

    print("x:\n", X)
    X.to_csv("comments.csv", index=False)
    re = pd.read_csv("comments.csv")

    for i in re['textDisplay']:
        print(i)
        sentiment_scores(i)