import youtubecomments as ytc
from wordcloud import wordcloud
import pandas as pd
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from colorama import Fore, Back, Style


def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print(Fore.LIGHTBLACK_EX+"*"*100)
    print(Back.LIGHTCYAN_EX+sentence+Style.RESET_ALL,"\n")
    print(Fore.RED+"sentences was rated as ==>", sentiment_dict['neg'] * 100, "% Negative")
    print(Fore.YELLOW+"sentences was rated as ==>", sentiment_dict['neu'] * 100, "% Neutral")
    print(Fore.GREEN+"sentences was rated as ==>", sentiment_dict['pos'] * 100, "% Positive")

    print(Fore.LIGHTBLUE_EX+"\nSentence Overall rated as", end=" ")

    if sentiment_dict['compound'] >= 0.05:
        print(Fore.GREEN+"Positive")
    elif sentiment_dict['compound'] <= -0.05:
        print(Fore.RED+"Negative")
    else:
        print(Fore.YELLOW+"Neutral")
    print(Fore.LIGHTBLACK_EX+"*"*100,)
    print(Style.RESET_ALL,"\n")

googleapikey="AIzaSyAwXKPmjC4WUBknPhLLWezOYoOaowYdujI"

videoid = input("Please Enter Video ID: ")

outputformat = "dataframe"

data = ytc.get_comments(googleapikey, videoid, outputformat)

cs = "result"

data.to_csv(cs,index = True)

df = pd.read_csv(cs)
title_words = list(df["textDisplay"].apply(lambda x: x.split()))
title_words = [x for y in title_words for x in y]
wc = wordcloud.WordCloud(width=1200, height=500,
                         collocations=False, background_color="Azure",
                         colormap="viridis").generate(" ".join(title_words))
plt.figure(figsize=(15,10))
plt.imshow(wc, interpolation="nearest")
_ = plt.axis("off")
plt.show()



if __name__ == "__main__":
    import pandas as pd

    dataset = pd.read_csv(cs)
    X = dataset['textDisplay']
    X.to_csv("comments.csv", index=True)
    re = pd.read_csv("comments.csv")

    for i in re['textDisplay']:
        sentiment_scores(i)
