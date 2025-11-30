import random

def word_gen(l):
    with open('words.txt') as f:
        all_words = f.read().splitlines()
        return random.choice([i for i in all_words if len(i) == l])
