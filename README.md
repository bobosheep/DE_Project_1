# Project 1 斷句
根據提供之新聞資料將所有文章內容做斷句，並將其排序、計算句子重複次數，最後以網頁型式呈現，並提供簡單搜尋功能。

## 系統環境
    *   OS: Win10 64-bit

    *   CPU: i5-8250U 1.6-3.4 GHz

    *   RAM: 8GB

    *   News data: 1.88 GB 

    *   Programming language: python

## 系統流程

1.  原資料處理
2.  斷句方法
3.  排序

###  1. 原資料處理
先把整個原始檔案做過濾，把我們需要的新聞文章內容取出來即可。

檔案內每篇新聞格式大致為下:
*   @Gais_REC
*   @url
*   @MainTextMD5
*   @UntagMD5
*   @SiteCode
*   @UrlCode
*   @title
*   @size
*   @keyword
*   @image_links
*   @Fetchtime
*   @post_time
*   @Ref
*   @BodyMD5
*   @Lang
*   @IP
*   @body

我們的目的是要取出新聞文章內容，也就是把格式中 @body 的內容取出來。取的方法是使用 python 的字串處理，把文件一行一行讀入，當該行句子開頭為 @body 時就開始取內容，並設立一個標記表示接下來的句子都是文章內容，直到出現 @ 開頭的句子。

程式碼如下
```python
for line in fp:              #檔案裡的句子
    if inbody :
        if line.startswith('@') :      
            #the end of the body
            inbody = False
            #print('finish')
            paragraphList += [paragraph]
        paragraph = paragraph + line

    if line.startswith('@body') :
        inbody = True
        paragraph = line.split(':')[1]
        article_count += 1
```

做完原資料處理後，可以得到 829,787 篇文章段落。
處理整個檔案花費 18.76 s，記憶體使用 6 MB 左右。

```javascript
Total articles: 829787
Time cost: 18.7663897 s
Memory cost: 6871992 bytes
Average time cost per article: 0.022615911914744387 ms
Average memory cost per article: 8.281633720460793 bytes
```


### 2. 斷句方法
將每篇新聞文章內容取出後就進行斷句。
我以以下正規表達式之內容進行斷句:
```python
r'[\?\!\！\？\。\;\；\|\｜\，\：][\」\》\）\)]?'
```
後半部的 ```[\」\》\）\)]?``` 是為了減少這些括號前被前面的標點符號段開，早成它多顯示在下一個句子的開頭，所以把它加進斷句的判斷。例如: "他說：「今天天氣真好！」我也覺得天氣很好"，最後一句 "我也覺得天氣很好" 前面就不會有 '」'。

斷句後的句子，我是利用 python 的 dictionary 型態的變數去做儲存，讓句子當作 key 去做重複的判斷， value 儲存出現次數。同時間也可以省去排序後的合併計算句子出現次數。
```python
{'句子1': 出現次數, '句子2': 出現次數}
```
斷完句子後，還要處理一些特別的符號以及不像句子的句子。例如句子裡包含 ★▲►▼● 這些奇怪的符號，我都把這些符號清掉，或是斷出一些太短的句子(我定義字串少於 3)，則當作例外做略過。

斷句處理程式碼如下
```python
for line in fp:     #前一個方法處理完所有新聞文章
    
    sentence = re.split(r'[\?\!\！\？\。\;\；\|\｜\，\：][\」\》\）\)]?', line)
    sentence_length = len(sentence)

    #處理斷出來的句子
    for s in sentence:
        
        #處理特殊字元
        s = ''.join(re.split('[\ \　\★\▲\►\▼\●\t\n\x00\x01\x08\x1c\x0b]', s))
        
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
```

斷句結果:
```javascript
Total sentences: 15,148,116
Split time cost: 129.0651037 s
Memory cost: 671,088,744 bytes
Average split time cost per sentence: 0.00852 ms
Average memory cost per sentence: 44.30179595 bytes

```

### 3. 排序

斷完所有句子後，接著就是進行排序。因為有了每個句子的出現次數，所以我的排序是根據句子的出現次數做排序，以出現次數多到少進行排序。
排序使用 python 內建函式 sorted()。此函式排序為 stable。
```python
sentences = [ v for v in sorted(sentences.items(), key = lambda x : x[1], reverse=True)]
```

排序出來的前10名如下:
```
('ETtoday東森新聞雲', 286792)
('ETlife東森生活雲', 195233)
('ETfashion時尚雲', 107200)
('ETtoday東森旅遊雲', 87428)
('娛樂星光雲', 83028)
('ETtoday新聞雲', 69341)
('ETtoday好朋友野餐日', 62202)
('88論壇', 46949)
('ET遊戲雲', 45611)
('東森新聞網2011年捲土重來', 36416)
```

排序結果:
```javascript
Total sentences: 15,148,116
Sort time cost: 4.7192817 s
Memory cost: 671,088,744 bytes
Average memory cost per sentence: 44.30179595 bytes
```

### 4. 網頁呈現
敬請期待 