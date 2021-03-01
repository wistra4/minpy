# 03_文字列を使う
'''
文字の集まりを文字列として扱う
'''

# 文字列を定義する
print("<文字列を定義する>")
'''
文字列の定義方法
"文字列"
'''
spam = "spam"
print(spam)
a_lylic = "でもね私のエネルギーは"
print(a_lylic)

# 文字列の凍結 
print("<文字列の凍結>")
'''
文字列と文字列を足し算すると連結できる
'''
a_lylic = a_lylic+"すでにインフィニティだよ"
print(a_lylic)

# 複合演算子
print("<複合演算子>")
lylic2 = "複合演算子を使ってみる"
lylic2 += "泣き顔見せるのを送ってた"
print(lylic2)

'''
演算子 / 説明
+= / 足し算、連結をして代入する
-= / 引き算をして代入する
*= / かけ算をして代入する
/= / 割り算をして代入する
'''

lylic3 = """強い人になろうとして
弱い僕を封じ込めて
ひとりぼっちになった"""
print(lylic3)

# 肩を揃えるPythonの流儀
'''
違うデータ型を足し算した場合のエラー
day = 24
date = day+"日"

Traceback (most recent call last):
  File "03.py", line 43, in <module>
    date = day+"日"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
# 文字列と数値の変換(型変換)
print("<文字列と数値の変換(型変換)>")
#str()関数を使う
day = 24     # 日付の数値
str_day = str(day)     # 数値を文字列に変換して変数に代入
date = str_day+"日"     # 文字列に変換した日付と文字列を連結する
print(date)
'''
組み込み関数
str()
int()
float()
'''
int("200")
float("3.1459265358979")