import numpy as np
import pandas as pd
pd.options.plotting.backend = "plotly"
import plotly.express as px
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA

def tsne_plot(words, word_vectors):
    "Creates a TSNE model and plots it"
    X = np.zeros(shape=(len(words), len(word_vectors[words[0]])))

    for idx, word in enumerate(words):
        X[idx] = word_vectors[word]

    pca = PCA(n_components=min(50, len(words)))
    X_50 = pca.fit_transform(X)

    tsne_model = TSNE(n_components=2, random_state=0, perplexity=len(words)-1)
    new_values = tsne_model.fit_transform(X_50)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])

    df = pd.DataFrame(dict(x=x, y=y, labels=words))
    fig = px.scatter(df, x="x", y="y", text='labels')
    fig.show()