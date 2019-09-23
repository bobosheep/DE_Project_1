
NEWS_DATA = './news_data/ettoday.rec'
Processed_data = './news_data/processed_data.rec'
paragraphList = []

with open(NEWS_DATA, 'r', encoding='utf-8', errors='ignore') as fp:
    inbody = False
    paragraph = ''
    article_count = 0
    for line in fp:
        if inbody :
            if line.startswith('@') :
                inbody = False
                #print('finish')
                #print(paragraph)
                paragraphList += [paragraph]
            paragraph = paragraph + line
        if line.startswith('@body') :
            inbody = True
            paragraph = line.split(':')[1]
            article_count += 1
            #print(paragraph)

    print(paragraphList[0])

with open(Processed_data, 'w', encoding='utf-8') as fp:
    fp.writelines(paragraphList)
