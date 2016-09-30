# -*- coding: utf-8 -*-
#import sys
import codecs
import re
'''
import codecs
with open("bocchan.txt",'r','utf_8') as b:
    s = b.read()
    s = s.replace("《[ぁ-ゞ]*》","")
    b.write(s)
"《[^》]+ 》""]》"
'''
if __name__ == "__main__":
    fin = codecs.open("sangoku8.txt","r")
    fout = codecs.open("sangoku2.txt", "w", "utf-8")
    s = fin.read()
    s = re.sub(r"《[ぁ-ゞ]*》","",s)
    print(s)
    fout.write(s)
