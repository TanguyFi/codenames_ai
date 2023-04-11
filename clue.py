from itertools import combinations

restrict_vocab=10000

def get_word_combinations(words, max_group_size):
    combination_groups = []
    for i in range(2, max_group_size + 1):
        combination_groups += [list(c) for c in combinations(words, i)]
    return combination_groups

def is_valid_word(word):
    return len(word) > 4

def get_clue_score(clue, clue_group, word_vectors):
    return sum(word_vectors.similarity(clue, word) for word in clue_group) / len(clue_group) + 0.02 * len(clue_group)

def get_clue_candidates(clue_group, word_vectors, radius=1000):
    clue_set = {}
    for word in clue_group:
        word_neighbours = word_vectors.most_similar(word, topn=radius, restrict_vocab=restrict_vocab)
        valid_neighbour_set = { word for (word, score) in word_neighbours if is_valid_word(word) }
        clue_set = valid_neighbour_set if len(clue_set) < 1 else clue_set & valid_neighbour_set

    scored_clues = [(clue, get_clue_score(clue, clue_group, word_vectors)) for clue in clue_set]
    return sorted(scored_clues, key= lambda x : -x[1])

def get_clue_groups(board, word_vectors, max_group_size=3):
    clue_groups = get_word_combinations(board['reds'], max_group_size)
    
    all_clues = []
    for clue_group in clue_groups:
        clue_candidates = get_clue_candidates(clue_group, word_vectors)

        if len(clue_candidates) > 0:
            clue = clue_candidates[0][0]
            score = clue_candidates[0][1]
        else:
            clue = None
            score = 0

        all_clues.append((clue_group, clue, score))

    return sorted(all_clues, key = lambda x : -x[2])

