import json
import re
from konlpy.tag import Twitter
from collections import Counter


# [a-zA-Z1-9]+ 정규표현식 알파벳 숫자 문자표현
# .* 모든문자열 표현
# [^\w] 공배 표현

def json_to_str(filename, key):
    jsonfile = open(filename, 'r', encoding='utf-8')
    json_string = jsonfile.read()
    jsonfile.close()

    data = ''
    json_data = json.loads(json_string)
    for item in json_data:
        value = item.get(key)
        if value is None:
            continue

        data += re.sub(r'[^\w]', '', value)

    return data


def count_wordfreq(data):
    twitter = Twitter()
    nouns = twitter.nouns(data)

    count = Counter(nouns)
    return count
