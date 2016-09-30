import sys
import random
import MeCab
from collections import defaultdict
def for_ngram(string):
    s = "。 "+"。 "+string
    return s
def for_ngram2(string):
    s = "。 "+string
    return s
def kei(string):
    words = []
    m = MeCab.Tagger('-Owakati')
    string = m.parse(string)
    print(string)
    for word in string.split():
        words.append(word)
    return words
def gram2(n, lis):
    result = defaultdict(list)
    for i in range(len(lis)-1):
        result[lis[i]].append(lis[i+1])
    return result

def gram3(n, lis):
    result = defaultdict(list)
    for i in range(len(lis)-2):
        result[lis[i]+lis[i+1]].append(lis[i+2])
    return result

def make_sentence(a, a2, n):
    words = []
    words.append("。")
    words.append(random.choice(a2["。"]))
    for i in range(n):
        words.append(random.choice(a[words[i] + words[i+1]]))
    stri = " ".join(words)
    stri = stri.replace(" 。", "。")
    stri = stri.replace(" 、", "、")
    stri = stri.replace(" ", "")
    print(stri[1:])
def make_sentence2(a, n):
    words = []
    words.append("。")
    for i in range(n):
        words.append(random.choice(a[words[i]]))
    stri = " ".join(words)
    stri = stri.replace(" .", ".")
    stri = stri.replace(" ,", ",")
    stri = stri.replace(" ","")
    print(stri[1:])
    
with open("test.txt") as f:
    s = f.read()
    
w = ""
k = for_ngram(s)
w = kei(k)
g = gram3(2,w)

w2 = ""
k2 = for_ngram2(s)
w2 = kei(k2)
g2 = gram2(2,w2)

while(input()):
    if(input() == "3"):
        make_sentence(g, g2, 40)
    else:
        make_sentence2(g2,40)
