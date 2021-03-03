# 10_Pythonの文字列と日本語
# バイト(bytes)型
s = "あいうえお"     # ひらがなを含む文字列型を定義
len(s)     # 長さを調べる

bs = s.encode("shift-jis")     # 文字列型からバイト型に変換
len(bs)     # 長さを調べる

print(bs)     # バイト型をprint()する
print(s[0])
print(bs[0])

# 文字列をバイト型に変換する
u = s.encode("euc-jp", "strict")     # EUC-JPの文字列に変換

# バイト型を文字列型に変換する
u = s.decode("shift-jis", "ignore")     # シフトJIS相当のバイト型を文字列型に変換

# スクリプトファイルのエンコード指定
# coding: エンコード名
# coding=エンコード名
# -*- coding: エンコード名 -*-
# coding: utf-8

# エンコードの判定
print("<エンコードの判定>")
def guess_encoding(s):
    """
    バイト型の文字列を引数として受け取り、
    エンコードを安易に判定する
    """
    # 判定を行うエンコードをリストに保存
    encodings = ["ascii", "utf-8", "shift-jis", "euc-jp"]
    for enc in encodings:
        try:
            s.decode(enc)     # エンコード変換を試みる
        except UnicodeDecodeError:
            continue     # エンコード変換に失敗したので次を試す
        else:
            return enc
            # エラーが発生しなかったら変換に成功したエンコードを返す
    else:
        return ""     # 成功したエンコードがなければから文字列を返す
        