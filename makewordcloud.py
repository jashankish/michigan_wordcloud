import sys
from os import path

from PIL import Image       # needed for cloud image

import wikipedia
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

# get path to script's directory
currdir = path.dirname(__file__)

def get_wiki(search):
    # find best title given a search
    title = wikipedia.search(search)[0]

    # select page
    page = wikipedia.page(title)
    return page.content     # the entire page content

def create_wordcloud(text):
    # create set of stopwords
    stop_words = ["university", "michigan", "campus"] + list(STOPWORDS)

    # create numpy array for image (cloud)
    mask = np.array(Image.open(path.join(currdir, "blockm.jpeg")))

    # create wordcloud object
    wc = WordCloud(background_color="white",
                   max_words=200,
                   mask=mask,
                   stopwords=stop_words)

    # generates wordcloud, still can't SEE it though
    wc.generate(text)

    # must SAVE wordcloud to view it
    wc.to_file(path.join(currdir, "wc.png"))

# Main
create_wordcloud(get_wiki(("University of Michigan")))

