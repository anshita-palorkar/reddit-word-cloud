import praw
from praw.models import MoreComments
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

url = str(input("Enter URL of Reddit thread:\n"))

#api auth
reddit = praw.Reddit(client_id="client id",
                     client_secret="client secret",
                     password="pwd",
                     user_agent="agent name",
                     username="user")

print("Scraping using account " + str(reddit.user.me()) + " ...")

#scraping comments from input url
submission = reddit.submission(url=url)
submission.comment_sort = "top"

comment_list = []
num = 0
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    comment_list.append(comment.body)
    num += 1

text = (" ").join(comment_list)

#cleaning collected text
text.lower()
punct = '-?!.,><~_=+*&^%$#@`""/;:[(){}\\]'
for char in punct:
    if char in text:
        text = text.replace(char, "")

#building word cloud
def plot_cloud(wordcloud):
    plt.figure(figsize = (12, 9))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

wordcloud = WordCloud(width = 3000, height = 2000, random_state=1,
            background_color='black', colormap='magma', font_path = "font path",
            collocations=False, stopwords = STOPWORDS).generate(text)

plot_cloud(wordcloud)

print("All done! " + str(num) + " comments were extracted.")
