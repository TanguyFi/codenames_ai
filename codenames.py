import random

def load_codenames_words(word_vectors):
    all_words = []
    with open('./codenames_words.txt', 'r') as f:
        for line in f:
            all_words.append(line.strip())
    
    return [word for word in all_words if word in word_vectors.index_to_key]


def get_board(all_words, seed=0):
    random.seed(seed)
    board_words = random.sample(all_words, 25)
    reds = board_words[0:9]
    blues = board_words[9:17]
    neutrals = board_words[17:24]
    assasins = [board_words[24]]
    
    return {
        "reds": reds,
        "blues": blues,
        "neutrals": neutrals,
        "assasins": assasins,
    }