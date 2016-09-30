import MeCab
import sys
lis =[]
s = "これは日本語環境のテストになっています。形態素解析結果の文字列を表示します"
m = MeCab.Tagger('-Owakati')
li = m.parse(s)
print(li)
