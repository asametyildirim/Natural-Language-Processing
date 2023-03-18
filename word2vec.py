import numpy as np
from gensim.models import Word2Vec
from sklearn.monifold import TSNE
import matplotlib.pyplot as plt

# prepare data
f = open('dataset.txt', 'r', encoding='utf8')
text = f.read()
t_list = text.split('\n')


corpus = []

# put sentences in list
for sentence in t_list:
 corpus.append(cumle.split())

#print to screen
print(corpus[:10])


#train model
model = Word2Vec(corpus, size=100, window=5, min_count=5, sg=1)

#test model
model.wv['Ankara']
model.wv.most_smilar('Turkiye')
