# -*- conding: utf-8 -*-
 
from konlpy.tag import Okt
import texttext
import os
import networkx
import re
import docx2txt


text_result = docx2txt.process("/Users/munyeonglee/nlp/2번최종연습.docx")
f = open("/Users/munyeonglee/nlp/fireinthehole.txt","r")
#stop_words = f.read()
#stop_word = stop_words.split("\n")


#309개의 태그를 가져오기. 그리고 형태에 맞추기 위해서 replace을 활용하여 짜름.
f = open("/Users/munyeonglee/nlp/tag.txt","r")
tag = f.read()
tag = tag.replace("\n","")
tag = tag.replace('"',"")
tag = tag.replace('[',"")
tag = tag.replace(']',"")
tag = tag.replace(" ","")
tag = tag.split(",")
# -*- coding: cp949 -*- 
sent=text_result

#불용어 : 이게 저를 가장 힘들게 한건데, 불용어를 사용하지 않으면 이상한 값들도 가져오는 경우가 많았기때문에, 이건 사용자가 늘리든 앞으로 이 코드를 만질 사람이 하든 점차 이걸 입력하고 빼면서 완성해주셨으면 좋겠습니다.

stop_word1 = list(set([('증폭기','Noun'),('고령자','Noun'),('상기','Noun'),('이루', 'Noun'),('정밀도', 'Noun'),('성하', 'Noun'),('가능', 'Noun'),('이송', 'Noun'),('위해', 'Noun'),('관련', 'Noun'),('도로', 'Noun'),('미관', 'Noun'),('도시 가스', 'Noun'),('가스', 'Noun'),('유류', 'Noun'),('상하', 'Noun'),('제적', 'Noun'),('설계도', 'Noun'),('진행', 'Noun'),('기반시설', 'Noun'),('판단', 'Noun'),('미관', 'Noun'),('증가', 'Noun'),('전기', 'Noun'),('파악', 'Noun'),('대부분', 'Noun'),('작업', 'Noun'),('문제점', 'Noun'),('이용', 'Noun'),('설치', 'Noun'),('로써', 'Noun'),('형태', 'Noun'),('파손', 'Noun'),('내부', 'Noun'),('공급', 'Noun'),('검사', 'Noun'),('매설', 'Noun'),('결함', 'Noun'),('시설', 'Noun'),('지하', 'Noun'),('거나', 'Noun'),('이나', 'Noun'),('천이', 'Noun'),('기존', 'Noun'),('입니', 'Adjective'),('자의', 'Noun'),('대한','Noun'),('물의','Noun'),('있는', 'Adjective'),('어서', 'Noun'),('만큼', 'Noun'),('면서', 'Noun'),('착용', 'Noun'), ('신호', 'Noun')]))
stop_word2 = list(set([('이상','Noun'),('유지','Noun'),('관리','Noun'),('촬영','Noun'),('노인','Noun'),('약자','Noun'),('현재','Noun'),('사건','Noun'),('기준','Noun'),('사고','Noun'),('다른','Noun'),('공정','Noun'),('장비','Noun'),('통해','Noun'),('상당','Noun'),('수의', 'Noun'),('비용','Noun'),('지출','Noun'),('소요','Noun'),('지연','Noun'),('실내','Noun'),('사회','Noun'),('사용자','Noun'),('이동','Noun'),('불편','Noun'),('속도','Noun'),('종류','Noun'),('금방','Noun'),('소진','Noun'),('가정','Noun'),('위치','Noun'),('통신','Noun'),('인구','Noun'),('직접','Noun'),('해주','Noun'),('전동','Noun'),('휠체어','Noun'),('생김새','Noun'),('다양','Noun'),('복지','Noun'),('소한','Noun'),('각종','Noun'),('등록','Noun'),('특허','Noun'),('번갈아','Noun'),('보행','Noun'),('사용','Noun'),('회전','Noun'),('발생','Noun'),('고정','Noun'),('형성','Noun'),('방향', 'Noun'),('기능', 'Noun'),('각각', 'Noun'),('패턴', 'Noun'),('구성', 'Noun'),('경우', 'Noun'),('도록',' Noun')]))
stop_word3 = list(set([('도록','Noun'),('양하','Noun'),('더욱','Noun'),('이로','Noun'),('오류로','Noun'),('사람','Noun'),('지지','Noun'),('로서','Noun'),('지원','Noun'),('역할','Noun'),('분야','Noun'),('적용','Noun'),('균형','Noun'),('조이스틱','Noun'),('고령화','Noun'),('머리','Noun'),('장애인','Noun'),('장애물','Noun')]))
#set으로 담을수 있는 양이 제한되어 있어서 초과될때마다 하나씩 추가해서 더해주는 방식으로 함
stop_word = set(stop_word1 + stop_word2 + stop_word3)


#('진행', 'Noun'),
#tr = texttext.TextRank()
#tagger = Okt()
#tr.loadSents(texttext.RawSentence(sent),
#             lambda sent: filter(lambda x: len(x[0])>=2 and x[1] in ('Noun', 'Verb', 'Adjective'), tagger.pos(sent)))
#tr.build()
#ranks = tr.rank()
#delete_sent=[]
#for k in sorted(ranks, key=ranks.get, reverse=True)[:100]:
#    print("\t".join([str(k), str(ranks[k]), str(tr.dictCount[k])]))
#    wow = str(tr.dictCount[k])
#    delete_sent.append(wow)
#cy = list(tr.dictCount.values())
#delsent = delete_sent[-int(len(tr.dictCount) * 0.1):-1]
#delsent.append(delete_sent[-1])
#for i in range(0,len(delsent)):
#    sent = sent.replace(delsent[i],'')

# 핵심어 뽑기 -> window, coef, 단어의 품사, 전체 단어 비율을 조절할 수 있다.
tr = texttext.TextRank(window=5, coef=1)
#tr.load(texttext.RawTagger(sent),lambda w: w not in stop_word and len(w[0])>=2 and w[1] in ('Noun'))
tr.load(texttext.RawTagger(sent), lambda w: w not in stop_word and len(w[0]) >=2 and w[1] in ('Noun'))

tr.build()
print(tr)
kw = tr.extract(0.3)
print("||||||")
print(kw)
print("~~~~~~~")
for k in sorted(kw, key=kw.get, reverse=True):
    print("%s\t%g" % (k, kw[k]))



for i in kw.keys():
    text = str(i).split(',')[0]
    text.replace("'"," ")
    text.replace('(',' ')
    text=text[2:len(text)-1]
    index = text_result.find(text)
    if text_result[index+len(text)] == " ":
        print(i, "통과")
    else:
        print(i, "안통과")




wow = []
for k in kw.keys():
    if len(k) == 2:
        ee = k[0][0] + k[1][0]
        wow.append(ee)
    else:
        ee = k[0][0]
        wow.append(ee)




