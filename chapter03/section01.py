# 01_ディクショナリ(辞書) を使う
purple = ["れにちゃん", "神奈川県", "感電少女"]

# ディクショナリ
'''
ディクショナリの定義方法
{キー1:値1, キー2:値2 ...}
'''
purple = {"ニックネーム": "れにちゃん",
          "出身地": "神奈川県",
          "キャッチフレーズ": "感電少女"}
        
# キーを使って要素を取り出す
print("<キーを使って要素を取り出す>")
'''
ディクショナリの要素を取り出す記法
ディクショナリ名[要素のキー]
'''
print(purple["出身地"])

print(purple)

# キーを使って要素を入れ替える
print("<キーを使って要素を入れ替える>")
purple["キャッチフレーズ"] = "鋼少女"
print(purple)

# 新しいキーと値を追加する
print("<新しいキーと値を追加する>")
purple["生年月日"] = "1993年6月21日"
print(purple)

# キーを使って要素を削除する
print("<キーを使って要素を削除する>")
del purple["ニックネーム"] 
print(purple) 

# print(purple["ニックネーム"])
'''
Traceback (most recent call last):
  File "section01.py", line 38, in <module>
    print(purple["ニックネーム"])
KeyError: 'ニックネーム'
'''

# キーの存在確認
print("<キーの存在確認>")
def convert_number(num):
    # アラビア数字とローマ数字の対応表をディクショナリに定義
    roman_nums = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
    # ディクショナリのキーとして引数の整数が存在していたら
    # キーに対応する値を戻り値にする
    if num in roman_nums:
        return roman_nums[num]
    else:
        return "[変換できません]"

print(convert_number(0))
print(convert_number(1))
print(convert_number(2))
print(convert_number(3))
print(convert_number(4))
print(convert_number(5))
print(convert_number(6))
print(convert_number(7))
print(convert_number(8))
print(convert_number(9))
print(convert_number(10))

# キーを使ったループ
print("<キーを使ったループ>")
purple= {"ニックネーム": "れにちゃん",
          "出身地": "神奈川県",
          "キャッチフレーズ": "感電少女",
          "生年月日": "1993年6月21日"}
for key in purple:     # キーをすべて取り出す
    print(key, purple[key])
