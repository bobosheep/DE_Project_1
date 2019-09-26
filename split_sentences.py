import re
import hashlib
import sys
import time
import pickle
import json

md5 = hashlib.md5()
break_data = './news_data/processed_data.rec'
sentences = {}
lines_count = 0


start = time.clock()

with open(break_data, 'r', encoding='utf-8', errors='replace') as fp:
    file_count = 0
    for line in fp:     #前一個方法處理完所有新聞文章
        
        sentence = re.split(r'[\?\!\！\？\。\;\；\|\｜\，\：][\」\》\）\)]?', line)
        sentence_length = len(sentence)

        #處理斷出來的句子
        for s in sentence:
            
            #處理特殊字元
            s = ''.join(re.split('[\ \　\★\◄\▲\►\▼\●\t\n\x00\x01\x08\x1c\x0b]', s))
            
            #不符合的句子都略過
            if s.startswith('20') or s.startswith('>') or s.startswith('\"') or s.startswith(',') or \
               s is '' or s is '\n' or len(s) <= 3:
                continue

            # sentences 為 dictionary 型態
            # 若沒有符合的 key 就加進 dictionary
            if sentences.get(s) is None:
                sentences[s] = 1
            else:
                sentences[s] += 1




        lines_count += 1
        #if lines_count % 5000 == 0: 
            #print('Processed {} datas'.format(lines_count))
            #print(sentences)

end = time.clock()

mem_cost = sys.getsizeof(sentences)
split_time_cost = end - start
sentence_count = len(sentences)

print('finish break sentence')
print("total {} lines".format(lines_count))
print("total {} sentences".format(sentence_count))

start = time.clock()
sentences = [ v for v in sorted(sentences.items(), key = lambda x : x[1], reverse=True)]
end = time.clock()

sort_time_cost = end - start

items = sentences
count = 0
for item in items:
    print(item)
    count += 1
    if count == 10 :
        break

sentence_array = []

with open('./news_data/sentences.rec', 'w', encoding='utf-8') as fp:
    for sentence_result in sentences:
        fp.write(sentence_result[0] + ': ' + str(sentence_result[1]))
        sentence_array.append({"name":sentence_result[0], "count": sentence_result[1]})
        fp.write('\n')

sentence_in_json = {"sentences": sentence_array}

with open('./news_data/sentences.bdata', 'wb') as fp:
    pickle.dump(sentences, fp)

with open('./news_data/sentences.json', 'w') as fp:
    json.dump(sentence_in_json, fp)

with open('split_sentences.info', 'w') as fp:
    fp.write('Total sentences: ' + str(sentence_count) + '\n')
    fp.write('Split time cost: ' + str(split_time_cost) + ' s\n')
    fp.write('Sort time cost: ' + str(sort_time_cost) + ' s\n')
    fp.write('Memory cost: ' + str(mem_cost) + ' bytes\n')
    fp.write('Average split time cost per sentence: ' + str(split_time_cost / sentence_count * 1000) + ' ms\n')
    fp.write('Average sort time cost per sentence: ' + str(sort_time_cost / sentence_count * 1000) + ' ms\n')
    fp.write('Average memory cost per sentence: ' + str(mem_cost / sentence_count) + ' bytes\n')

#sentences.sort()
#print(sentences)