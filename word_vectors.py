from gensim.models import KeyedVectors

def load_word_vectors():
    datafile = "./models/frWiki_no_phrase_no_postag_1000_skip_cut100.bin"

    word_vectors = KeyedVectors.load_word2vec_format(datafile, binary=True, unicode_errors="ignore")
    word_vectors.sort_by_descending_frequency()
    return word_vectors



