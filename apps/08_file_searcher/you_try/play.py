import os
import collections

file = '/Users/danielspector/Documents/txt/5.txt'
text = 'the'

SearchResult = collections.namedtuple('SearchResult',
                                      'file, line, text')

matches = []

with open(file, 'r', encoding='utf-8') as fin:
    for num, line in enumerate(fin, 1):
        search = SearchResult(line=line_num, file=file, text=text)
        matches.append(search)
