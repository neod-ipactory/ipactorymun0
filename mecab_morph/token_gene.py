#!/usr/bin/python3
# -*- coding: utf-8 -*-
# import python lib

import pyperclip
import codecs
import os
import datetime
import re
import time
# project path import
import config
# import project lib
import MeCab
import editdistance
# import project model
from jaso_convert import ko_jaso
from mecab_parser import mecab_morph_parser

import docx2txt
from collections import Counter

text_result = docx2txt.process("/Users/munyeonglee/nlp/최종8번.docx")


# N 명사 , V 동사/형용사, S 숫자,영어 등 ETC
noun_verb_other = ["N","V","S"]
# J 조사 , E 어미, X 접미사, M 관형사 감탄사
josa_eomi = ["J","E","X","M"]
class morph_data:
    def __init__(self):
        # db connection create
        #self.mysql_conn = mysql_connector.mysql_model(connection_info.CONN_NEW_INFO)
        #self.mysql_conn.create_connection()
        #self.patent_model = patent_model.patent(self.mysql_conn)
        self.morph_parse = mecab_morph_parser()
    # \n\r 제거
    def replace_cr(self, text):
        text.replace("\n", "  ")
        text.replace("\r", "  ")
        return text
    # get word
    def get_noun_verb_words(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["N","V","S"]:
                word_list.append(element["word"])
        word_str = ",".join(word_list)
        return word_str
    # get word
    def get_noun_verb_josa_eomi_words(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["N","V","S","J","E"]:
                word_list.append(element["word"])
        word_str = ",".join(word_list)
        return word_str
    def get_noun_verb_jaso_words(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["N","V","S"]:
                word_list.append(self.get_jaso_word(element["word"]))
        word_str = ",".join(word_list)
        return word_str
    # get word
    def get_noun_words(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["N"]:
                word_list.append(element["word"])
        word_str = ",".join(word_list)
        return word_str
    # get word
    def get_verb_words(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["V"]:
                word_list.append(element["word"])
        word_str = ",".join(word_list)
        return word_str
    def get_eomi_word(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["J","E","X","M"]:
                word_list.append(element["word"])
        word_str = ",".join(word_list)
        return word_str
    def get_eomi_jaso_word(self, sentence):
        morph_parse = self.morph_parse.parse_morph(sentence)
        word_list = []
        for element in morph_parse:
            if element["morph"] in ["J","E","X","M"]:
                word_list.append(self.get_jaso_word(element["word"]))
        word_str = ",".join(word_list)
        return word_str
    def get_jaso_word(self, sentence):
        return ko_jaso(sentence)
    # get word ngram
    def get_ngram_words(self, sentence):
        convert_tuple = tuple(sentence)
        result_str = ""
        result_str += (','.join(ngram_tuple[0] for ngram_tuple in list(convert_tuple)))
        return result_str
if __name__ == "__main__":
    # program start
    VAR_PATH = os.path.dirname(os.path.realpath(__file__))+"/var"
    train = morph_data()
    morph_parse = mecab_morph_parser()
    run_time = datetime.datetime.now()

    noun_verb_other = ["N","V","S"]
    # J 조사 , E 어미, X 접미사, M 관형사 감탄사
    josa_eomi = ["J","E","X","M"]


    #ab = str(re.compile('[a-zA-Z]+').findall(text_result))

    #ab = ab[1:len(ab)-1]
    #for char in "'?!/ ":
    #    ab = ab.replace(char,"")

    #morph_text = train.get_noun_words(text_result)
    ab = str(re.compile('[a-zA-Z]+').findall(text_result))
    ab = ab[1:len(ab)-1]
    for char in "'?!/ ":
        ab = ab.replace(char,"")
    morph_text = train.get_noun_words(text_result)+','+ab

    a = 1
    arr = []
    morph_text.replace(" ","")
    b = morph_text.split(",")


    text_result = docx2txt.process("/Users/munyeonglee/nlp/최종8번.docx")

    #명사로만 가져온것을 ,로 구분
    find_list = b
    
    
    for word in find_list:
        pattern = re.compile(word)
        result_regex = pattern.finditer(text_result)
        print(word)
        arr.append(word)

    new_arr = []



    #중복 제거
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    print(new_arr)


    index_arr = []
    count = 0

    result = []
    for i in range(len(new_arr)):
        for j  in range(len(new_arr)):
            if i == j:
                continue
            else:
                index_arr.append((i, j))



    for i in range(len(index_arr)):
        temp_txt = new_arr[index_arr[i][0]] + new_arr[index_arr[i][1]]
        temp_txt2 = new_arr[index_arr[i][0]] + " " + new_arr[index_arr[i][1]]
        result.append(temp_txt)
        result.append(temp_txt2)
    tags = []


    result_list = []
    text_result1 = docx2txt.process("/Users/munyeonglee/nlp/최종8번.docx")

    print(new_arr)

    #print(result)

    for i in result:
        if i in text_result1:
            result_list.append(i)
    print(result_list)


