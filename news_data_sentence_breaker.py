import re
import hashlib

md5 = hashlib.md5()
break_data = './news_data/processed_data.rec'
saved_data = './news_data/sentences_{}.rec'
sentences = {}
lines_count = 0

with open(break_data, 'r', encoding='utf-8', errors='replace') as fp:
    file_count = 0
    for line in fp:
        
        '''
        if(count == 1000):
            file_count += 1
            count = 0
        with open(saved_data.format(file_count), 'a+', encoding='utf-8') as savedfp:    
        '''
        sentence = re.split(r'[\?\!\！\？\。\;\；\|\｜\，\：][\」\》\）\)]?', line)
        
        
        sentence_length = len(sentence)

        '''
        for i in range(0, sentence_length - 1, 2):
            sentence[i] = sentence[i] + sentence[i + 1]

        if lines_count < 5:
            print('after:')
            print(sentence)
        '''

        for s in sentence:
            
            s = ''.join(s.split(' '))
            s = ''.join(s.split('　'))
            s = ''.join(s.split('★'))
            s = ''.join(s.split('▲'))
            s = ''.join(s.split('►'))
            s = ''.join(s.split('▼'))
            s = ''.join(s.split('>>>'))
            s = ''.join(s.split('\n'))
            s.replace('', '')
            s.replace('▲', '')
            s.replace('►', '')
            if s.startswith('20') or s.startswith('>') or s.startswith(',') or s is '' or s is '\n' or s is '、' or\
               s.startswith(' ') or s.startswith('?') or s.startswith('!') or s.startswith('|') or\
               s.startswith('？') or s.startswith('！') or s.startswith('｜') or s.startswith('。') or\
               s.startswith('；') or s.startswith(';') :
                continue

            #md5.update(s.encode('utf-8'))
            #encode_s = md5.hexdigest()

            if sentences.get(s) is None:
                sentences[s] = 1
            else:
                sentences[s] += 1

            #print(s)
            #sentences += s
            #savedfp.write(s)

            if lines_count < 10:
                print(s)


        lines_count += 1
        if lines_count % 5000 == 0:
            print('Processed {} datas'.format(lines_count))
            #print(sentences)

print('finish break sentence')
print("total {} lines".format(lines_count))
print("total {} sentences".format(len(sentences)))

sentences = [ v for v in sorted(sentences.items(), key = lambda x : x[1], reverse=True)]

items = sentences
count = 0
for item in items:
    print(item)
    count += 1
    if count == 10 :
        break

with open('./news_data/sentences.rec', 'w', encoding='utf-8') as fp:
    for sentence_result in sentences:
        fp.write(sentence_result[0] + ': ' + str(sentence_result[1]))
        fp.write('\n')

#sentences.sort()
#print(sentences)