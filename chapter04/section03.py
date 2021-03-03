# 03_文字列型を使いこなす
# 文字列の置換と削除
print("<文字列の置換と削除>")
orig_str = "いっぱい"     # 置換前の文字列を定義
orig_str.replace("い", "お")     # 文字列の「い」を「お」に置換、結果を表示
print(orig_str)

str_num = "1,000,000"     # カンマの入った整数相当の文字列
num = int(str_num.replace(",", ""))
print(num)

# aplit()メソッドとjoin()メソッド
import matplotlib.pyplot as plt

str_speeds = "38 42 20 40 39"     # 戦車の速度(km/h)
str_armor = "80 50 17 50 51"     # 戦車の装甲厚(mm)
speeds = str_speeds.split(" ")     # 速度をスペースで分割
armors = str_armor.split(" ")     # 装甲厚をスペースで分割
markers = ["o", "v", "^", "<", ">"]     # グラフ上のマーク

for idx in range(len(speeds)):     # リストの長さ分ループ
    x = int(speeds[idx])     # 文字列を数値に変換
    y = int(armors[idx])
    plt.scatter(x, y, marker=markers[idx])     # 散布図を書く
plt.show()
# IV号戦車(o) LT-38(v) 八九式中戦車(^) III号突撃砲(<) M3中戦車(>)

str_speeds = "38 42 20 40 39"     # 空白で区切られた数値
speeds = str_speeds.split()     # 空白で分割
csep_speeds = ",".join(speeds)     # カンマで連結
print(csep_speeds)     # 結果を表示

str_speeds2 = " 38  42 20 40 39 "     # 余分な空白が入った文字列
print(str_speeds2.replace(" ", ","))     # replace()を使った結果を表示

str_speeds2 = " 38  42 20 40 39 "     # 余分な空白が入った文字列
speeds2 = str_speeds2.split()     # split(),join()を使って置換
csep_speeds2 = ",".join(speeds2)
print(csep_speeds2)     # 結果を表示

# エスケープシーケンス
print("<エスケープシーケンス>")
def func():     # func()関数の定義
    words = """ゆく河の流れは絶えずして
しかももとの水にあらず"""     # 改行を含む文字列を変数にする
    print(words)
func()     # func関数の実行

def func():
    words = "ゆく河の流れは絶えずして¥nしかももとの水にあらず"
    print(words)
func()

'''
エスケープシーケンスの一覧(よく使われるもの)
エスケープシーケンス / 説明
¥n / 改行
¥r / 改行(CR、キャリッジ・リターン)
¥t / 水平タブ
¥f / 改ページ(フォーム・フィード)
¥' / シングルクォーテーション
¥" / ダブルクォーテーション
¥¥ / バックスラッシュ
¥x61 / 16進数に対応する8ビット文字
¥u3042 / 16ビット16進数に対応するUnicode文字、16進数部分には「0x」は不要
¥0 / Null文字
'''

# raw文字列
print("<raw文字>")
raw = r"C:¥path¥to¥file"
print(raw)

# 文字列のフォーマット
print("{} loves Python !".format("Guido"))

linkstr = '<a href="{}">{}</a>'
for i in [ 'http://python.org',
           'http://pypy.org',
           'http://cython.org',]:
           print(linkstr.format(i, i.replace('http://', '')))

# 引数の順番を指定した置換
print("{0} {1} {0}".format('Spam', 'Ham'))
# キーワード引数を指定した置換
print("{food1} {food2} {food1}".format(food1='Spam', food2='Ham'))
# ディクショナリを指定した置換
d = {'name':'Guido', 'birthyear':1964}
print("{0[birthyear]} is {0[name]}'s birthyear.".format(d))
# sysモジュールのversionアトリビュートを使ってPythonのバージョンを表示する
import sys     # sysモジュールをインポート
print("Python version: {0.version}".format(sys))
# 寄せを指定して差し込む
tmp1 = "{0:10} {1:>8}"     # 1つ目の要素を左寄せで、2つ目の要素を右寄せで置換
print(tmp1.format('Spam', 300))
print(tmp1.format('Ham', 200))
# 表記を指定して差し込む
print("{:.2%}".format(6381/12708))
print("{:,}".format(10000))
# f文字列
name = "君"     # 置換する要素を変数で定義
print(f"まずは{name}が落ち着け")     # [name]の部分が変数の内容に置き換わる