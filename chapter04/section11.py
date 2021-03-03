# 11_Pythonのファイル管理
# ファイルとファイルオブジェクト
f = open("foo.txt", 'r', encoding='utf-8')     # ファイルを開く
s = f.read()     # ファイルの内容を文字列型の変数に読み込む
print(s)     # ファイルの内容を表示する
f.close()     # ファイルを閉じる

# ファイルから読み込む
f = open("test.txt", 'r', encoding='utf-8')     # ファイルを開く
for line in f:     # ファイルから1行ずつ読み込む
    print(line, end=" ")     # 1けたずつ表示する

# ファイルに書き込む
f = open("newfile.txt", "w", encoding="UTF-8")     # ファイルをモードwで開く
f.write(s)     # 変数sの文字列をファイルに書き出す
f.close()     # ファイルを閉じる

# バイナリファイルを扱う
imgfile = open('someimage.png', 'rb')
imgsrc = imgfile.read()
if imgsrc[1:4] == b'PNG':
    print('image/png')

# ファイル名の扱い
import sys     # sysモジュールをインポート
sys.getfilesystemencoding()