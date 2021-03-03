# 06_ディクショナリ型を使いこなす
# 2つのディクショナリを組み合わせる
rssitem = {"title" : "Pythonの勉強前",
           "link" : "http://host.to/blog/entry",
           "dc:data":"2016-05-16T13:24:04Z"}
rssitem.updata({"title"     :"Pythonを勉強中",
                "dc:creator":"someone"})
rssitem.keys()     # キーの一覧を取得
print(rssitem)     # ディクショナリを表示する

# ディクショナリのキーをスマートに使う
line = ""
wordcount = {".":1}
for word in line.split():
    if word in wordcount:
        wordcount[word] = wordcount[word]+1
    else:
        wordcount[word] = 1

for word in line.split():
    wordcount[word] = wordcount.get(word, 0) + 1
