import os
import sys
import re
import pandas as pd
import numpy as np


# import matplotlib.pyplot as plt

class Dialogue:
    '''
    对话类
    '''
    # 正则表达式
    # 1（国家-姓名） 或者 1-国家-姓名
    pattern = re.compile(r'^\d\s*[（(](.*)[）)]|^\d\s*-(.*)')

    def __init__(self, fpath):
        '''
        param fpath: 单个对话文件path
        '''
        with open(fpath) as f:
            raw_txt = f.read().replace(' ', '')
            self.count = len(raw_txt)
            self.lines = raw_txt.split()

        self.country = {}
        self.name = {}
        self.num = 0  # 对话人数
        self.data = pd.DataFrame(columns=('n_p', 'content'))
        self.fpath = fpath

    def __iter__(self):
        for i, line in self.data.iterrows():
            yield line

    def reset(self):
        self.country = {}
        self.name = {}
        self.num = 0  # 对话人数
        self.data = pd.DataFrame(columns=('n_p', 'content'))

    def handle(self):
        # 按行处理，提取国别、姓名，生成dateframe
        for line in self.lines:
            n_p = line[0]
            if not n_p.isdigit(): continue
            if n_p == '0':
                self.country[n_p] = '齐'
                self.name[n_p] = '-'
            if n_p not in self.country:
                #                 print(n_p, self.country)
                matched = self.pattern.search(line)
                if matched:
                    for m in matched.groups():
                        if m:
                            if '-' in m:
                                country, name = m.split('-', 1)
                            else:
                                country = m
                                name = country + n_p
                            self.country[n_p] = country
                            self.name[n_p] = name
            #             print({'n_p':n_p, 'content':line})
            self.data = self.data.append({'n_p': n_p, 'content': line}, ignore_index=True)
        self.num = len(self.country)
        if self.num == 0:
            print('no country!', self.fpath)


def gen_filepaths(dirpath):
    '''
    生成文件列表
    '''
    filepath_list = []
    for dirpath, dirnames, filenames in os.walk(dirpath):
        for filename in filenames:
            if filename.split('.')[-1] == 'txt':
                fpath = os.path.join(dirpath, filename)
                filepath_list.append(fpath)
    return filepath_list


def gen_dialogues(filepath_list):
    '''
    根据 文件列表 生成 对话列表
    '''
    dialogues = []
    n = len(filepath_list)
    for fpath in filepath_list:
        dialogue = Dialogue(fpath)
        dialogue.handle()
        dialogues.append(dialogue)
    return dialogues


def count_countries(dialogues):
    '''
    统计所有出现的国家
    '''
    countries = []
    for dialogue in dialogues:
        countries.extend(dialogue.country.values())
    return countries


def describe_dialogues(dialogues):
    '''
    生成描述，相应国家
    '''
    des_list = []
    count_total = 0
    for dialogue in dialogues:
        count_total += dialogue.count
        row = pd.DataFrame([[dialogue.country, dialogue.fpath]], columns=['国家', 'file'])
        des_list.append(row)
    des_df = pd.concat(des_list, ignore_index=True)
    print("总字数：", count_total)
    return des_df


def count_word_from_country(dialogues):
    '''
    统计每个国家对话的字数
    '''
    from collections import defaultdict
    word_from_country = defaultdict(lambda: 0)  # 统计 每个国家的对话的字数, 默认 0

    for dialogue in dialogues:
        for line in dialogue:
            country = dialogue.country[line.n_p]
            word_from_country[country] += len(line.content)
    return word_from_country

def check_country(dialogues):
    '''
    检查国家是否完整
    '''
    for dialogue in dialogues:
        A = set(dialogue.data.n_p)
        B = set(dialogue.country)
        if A != B:
            print(dialogue.fpath, A - B)


def find_word(dialogues, word, include=None, exclude=[]):
    '''
    从dialogues中查找 词组word.
    如果 include!=None，exclude不起作用
    '''
    results_list = []

    for dia_index, dialogue in enumerate(dialogues):
        for line in dialogue:
            country = dialogue.country[line.n_p]
            if include is not None:
                if country not in include: continue
            if exclude is not None:
                if country in exclude: continue

            if word in line.content:
                name = dialogue.name[line.n_p]

                result = pd.DataFrame([[country, name,
                                        dialogue.fpath, line.content, dia_index, line.name]],
                                      columns=['country', 'name', 'file', 'content','dia_index','index'])
                results_list.append(result)
    if results_list:
        results = pd.concat(results_list, ignore_index=True)
        return results
    else:
        return None


