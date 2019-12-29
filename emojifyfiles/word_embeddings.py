
import numpy as np

def read_glove_vecs():
    with open ('/home/nyle/Desktop/django/api/emojifyfiles/glove.6B.50d.txt', 'r') as f: 
        words = set()
        word_to_vec_map = {}
        for line in f:
            line = line.strip().split()
            curr_word = line[0]
            words.add(curr_word)
            word_to_vec_map[curr_word] = np.array(line[1:], dtype=np.float64)
        i = 1
        words_to_index = {}
        index_to_words = {}
        for w in sorted(words):
            words_to_index[w] = i
            index_to_words[i] = w
            i = i + 1
    

    import json

    with open('word_to_index.json', 'w') as fp:
        json.dump(words_to_index, fp)


    return words_to_index, index_to_words, word_to_vec_map


read_glove_vecs()




