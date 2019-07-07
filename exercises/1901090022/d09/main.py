from mymodule import stats_word
from collections import Counter
import json

json_file = open('/Users/adamlu/Documents/GitHub/selfteaching-python-camp/exercises/1901090022/d09/1001S02E09.json')
jason_data = json.load(json_file)

text = ""
for poetry in jason_data:
    text += poetry['contents']
word_list = stats_word.stats_text_cn(text, 100)
print(word_list)
'''
输出词频结果如下
[('不', 218), ('人', 203), ('山', 157), ('无', 127), ('日', 125), ('一', 123), ('月', 120), ('风', 119), ('天', 118), ('来', 108), ('云', 108), ('有', 101), ('夜', 101), ('上', 95), ('长', 95), ('何', 92), ('生', 91), ('君', 91), ('时', 90), ('相', 87), ('水', 86), ('江', 84), ('见', 83), ('花', 83), ('春', 80), ('如', 78), ('中', 77), ('行', 76), ('为', 75), ('青', 75), ('白', 73), ('明', 71), ('归', 71), ('下', 71), ('万', 70), ('自', 69), ('落', 69), ('秋', 67), ('空', 67), ('此', 65), ('之', 64), ('今', 63), ('里', 63), ('年', 63), ('去', 62), ('声', 61), ('未', 59), ('心', 58), ('欲', 58), ('家', 57), ('马', 57), ('三', 56), ('飞', 56), ('雨', 56), ('城', 56), ('在', 55), ('金', 55), ('客', 55), ('将', 55), ('清', 54), ('寒', 54), ('西', 53), ('处', 53), ('高', 52), ('事', 52), ('黄', 52), ('门', 52), ('朝', 52), ('十', 51), ('入', 50), ('是', 50), ('子', 50), ('知', 49), ('闻', 49), ('玉', 49), ('流', 49), ('开', 48), ('尽', 48), ('阳', 48), ('色', 48), ('古', 48), ('得', 47), ('我', 47), ('酒', 47), ('出', 47), ('道', 47), ('草', 46), ('千', 46), ('南', 45), ('与', 45), ('前', 45), ('深', 44), ('大', 44), ('独', 43), ('头', 42), ('海', 41), ('远', 41), ('可', 41), ('已', 40), ('问', 40)]
'''