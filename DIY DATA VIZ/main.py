import os
from os import path
from wordcloud import WordCloud

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

text = open(path.join(d, 'cars.csv')).read()

# Generate a word cloud
wordcloud = WordCloud().generate(text)

# Display the generated image:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(font_path = '/Library/Fonts/Arial Unicode.ttf', background_color="black", width=3000, height=3000, max_words=1000)

wordcloud = WordCloud(max_font_size=35).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()