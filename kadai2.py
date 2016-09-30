import sys
import random
from collections import defaultdict
def for_ngram(string):
    s = ". "+string
    sl = s.replace(".", " .")
    ss = sl.replace(",", " ,")
    return ss
def kei(string):
    words = []
    for word in string.split():
        words.append(word)
        #words.append(word.strip(".,?!"))
    return words
def ngram(n, lis):
    result = defaultdict(list)
    for i in range(len(lis)-1):
        result[lis[i]].append(lis[i+1])
    return result
def make_sentence(a, n):
    words = []
    words.append(".")
    for i in range(n):
        words.append(random.choice(a[words[i]]))
    stri = " ".join(words)
    stri = stri.replace(" .", ".")
    stri = stri.replace(" ,", ",")
    print(stri[2:])
with open("en.txt") as f:
    s = f.read()
s = for_ngram(s)
w = kei(s)
make_sentence(ngram(2, w), 30)
