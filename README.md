# Project 0.1 斷句與搜尋

<font size=4>根據提供之新聞資料將所有文章內容做斷句，並將其排序、計算句子重複次數，最後以網頁型式呈現，並提供簡單搜尋功能。</font>

## 系統環境
    *   OS: Win10 64-bit
    
    *   CPU: i5-8250U 1.6-3.4 GHz
    
    *   RAM: 8GB
    
    *   News data: 1.88 GB 
    
    *   Programming language: python

## 系統流程

1.  <font size=4>原資料處理</font>
2.  <font size=4>斷句方法</font>
3.  <font size=4>排序</font>

###  1. 原資料處理
<font size=4>先把整個原始檔案做過濾，把我們需要的新聞文章內容取出來即可。</font>

<font size=4>檔案內每篇新聞格式大致為下:</font>

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

<font size=4>我們的目的是要取出新聞文章內容，也就是把格式中 @body 的內容取出來。取的方法是使用 python 的字串處理，把文件一行一行讀入，當該行句子開頭為 @body 時就開始取內容，並設立一個標記表示接下來的句子都是文章內容，直到出現 @ 開頭的句子。</font>

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

<font size=4>做完原資料處理後，可以得到 829,787 篇文章段落。<br>
處理整個檔案花費 18.76 s，記憶體使用 6 MB 左右。</font>

```javascript
Total articles: 829787
Time cost: 18.7663897 s
Memory cost: 6871992 bytes
Average time cost per article: 0.022615911914744387 ms
Average memory cost per article: 8.281633720460793 bytes
Storage: 1.48 GB
```


### 2. 斷句方法
<font size=4>將每篇新聞文章內容取出後就進行斷句。<br>我以以下正規表達式之內容進行斷句:</font>

```python
r'[\?\!\！\？\。\;\；\|\｜\，\：][\」\》\）\)]?'
```
<font size=4>後半部的 ```[\」\》\）\)]?``` 是為了減少這些括號前被前面的標點符號段開，早成它多顯示在下一個句子的開頭，所以把它加進斷句的判斷。例如: "他說：「今天天氣真好！」我也覺得天氣很好"，最後一句 "我也覺得天氣很好" 前面就不會有 '」'。</font>

<font size=4>斷句後的句子，我是利用 python 的 dictionary 型態的變數去做儲存，讓句子當作 key 去做重複的判斷， value 儲存出現次數。同時間也可以省去排序後的合併計算句子出現次數。</font>

```python
{'句子1': 出現次數, '句子2': 出現次數}
```
<font size=4>斷完句子後，還要處理一些特別的符號以及不像句子的句子。例如句子裡包含 ★▲►▼● 這些奇怪的符號，我都把這些符號清掉，或是斷出一些太短的句子(我定義字串少於 3)，則當作例外做略過。</font>

<font size=4>斷句處理程式碼如下</font>

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

<font size=4>斷句結果:</font>

```javascript
Total sentences: 15,148,116
Split time cost: 129.0651037 s
Memory cost: 671,088,744 bytes
Average split time cost per sentence: 0.00852 ms
Average memory cost per sentence: 44.30179595 bytes
Storage: 683 MB
```

### 3. 排序

<font size=4>斷完所有句子後，接著就是進行排序。因為有了每個句子的出現次數，所以我的排序是根據句子的出現次數做排序，以出現次數多到少進行排序。
排序使用 python 內建函式 sorted()。此函式排序為 stable。</font>

```python
sentences = [ v for v in sorted(sentences.items(), key = lambda x : x[1], reverse=True)]
```

<font size=4>排序出來的前10名如下:</font>

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

<font size=4>排序結果:</font>

```javascript
Total sentences: 15,148,116
Sort time cost: 4.7192817 s
Memory cost: 671,088,744 bytes
Average memory cost per sentence: 44.30179595 bytes
```

### 4. 網頁呈現
<font size=4>網頁前端: **Angular + Angular Material</font>**

<font size=4>網頁後端: **Flask**</font>

#### 網站架構

![DE_Project_Web_structure](C:\Users\user\Documents\course\108-1\DataEngineering\DE_Project_1_report\DE_Project_Web_structure.png)

#### 搜尋頁面流程

![DE_Project_Web](C:\Users\user\Documents\course\108-1\DataEngineering\DE_Project_1_report\DE_Project_Web_system_arch.jpg)



#### 範例頁面

* <font size=4>home page</font>

  ![1570524866862](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570524866862.png)

* <font size=4>project description page</font>

  ![1570524904986](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570524904986.png)

* <font size=4>search interface page</font>

  ![1570524936690](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570524936690.png)

* <font size=4>performance data page</font>

  ![1570524981824](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570524981824.png)

* <font size=4>搜尋字詞</font>

  ![1570525047641](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570525047641.png)

* <font size=4>搜尋結果</font>

  ![1570525089683](C:\Users\user\AppData\Roaming\Typora\typora-user-images\1570525089683.png)