#!pip install -U scikit-learn scipy matplotlib

import numpy as np
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# prepare data
f = open('texts.csv', 'r', encoding='utf8')
text = f.read()
t_list = text.split('\n')


corpus = []

# put sentences in list
for sentence in t_list:
 corpus.append(sentence.split())

#print to screen
print(corpus[:10])


#train model
model = Word2Vec(corpus, size=100, window=5, min_count=5, sg=1)
#test model
model.wv['Ankara']
model.wv.most_similar('Türkiye')

#-----------------------------------------------------------------

#model save
model.save('save.model')

#model load
model = Word2Vec.load('save.model')

def closestwords_tsneplot(model,word):
	word_vectors = np.empty((0,100))
	word_labels = [word]
	
	close_words = model.wv.most_similar(word)
	
	word_vectors = np.append(word_vectors, np.array([model.wv[word]]), axis=0)
	
	for w, _ in close_words:
		word_labels.append(w)
		word_vectors = np.append(word_vectors, np.array([model.wv[w]]), axis=0)
		
	tsne = TSNE(random_state=0, perplexity=10)
	Y = tsne.fit_transform(word_vectors)
	x_coords = Y[:,0]
	y_coords = Y[:,1]
	
	plt.scatter(x_coords, y_coords)
	
	for label,x,y in zip(word_labels, x_coords, y_coords):
		plt.annotate(label, xy=(x,y), xytext=(5,-2), textcoords='offset points')
		
	plt.show()
	
	
closestwords_tsneplot(model, 'iş')
	
	
