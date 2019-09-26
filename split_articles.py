import sys
import time

NEWS_DATA = './news_data/ettoday.rec'
Processed_data = './news_data/processed_data.rec'
paragraphList = []

start = time.clock()

with open(NEWS_DATA, 'r', encoding='utf-8', errors='ignore') as fp:
    inbody = False
    paragraph = ''          #get the info of @body
    article_count = 0
    for line in fp:                         #lines in the file
        if inbody :
            if line.startswith('@') :       #the end of the body
                inbody = False
                paragraphList += [paragraph]
            paragraph = paragraph + line

        if line.startswith('@body') :       #the start of the body
            inbody = True
            paragraph = line.split(':')[1]
            article_count += 1

end = time.clock()

print('len of paragraphList: ' + str(len(paragraphList)))
totalSize = 0
for p in paragraphList:
    totalSize += sys.getsizeof(p)
    #print(str(sys.getsizeof(p)) + '  ' + p)

mem_cost = sys.getsizeof(paragraphList)
time_cost = end - start

with open(Processed_data, 'w', encoding='utf-8') as fp:
    fp.writelines(paragraphList)

print('mem cost = ' + str(mem_cost) + ', total size = ' + str(totalSize) )

with open('split_articles.info', 'w') as fp:
    fp.write('Total articles: ' + str(article_count) + '\n')
    fp.write('Time cost: ' + str(time_cost) + ' s\n')
    fp.write('Memory cost: ' + str(mem_cost) + ' bytes\n')
    fp.write('Average time cost per article: ' + str(time_cost / article_count * 1000) + ' ms\n')
    fp.write('Average memory cost per article: ' + str(mem_cost / article_count) + ' bytes\n')
