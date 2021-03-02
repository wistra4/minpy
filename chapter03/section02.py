# 02_set(集合)を使う
# setを定義する
'''
setを定義する記法
{要素, 要素, 要素}
'''
dice = {1, 2, 3, 4, 5, 6}
coin = {"表", "裏"}

# setの和集合を得る
print("<setの和集合を得る>")
prime = {2, 3, 5, 7, 13, 17}     # 素数のsetを定義
fib = {1, 1, 2, 3, 5, 8, 13}     # フィボナッチ数のsetを定義

prime_fib = prime | fib     # 2つの和集合を得る
print(prime_fib)     # 得られた和集合を表示

# setの差集合を得る
print("<setの差集合を得る>")
dice = {1, 2, 3, 4, 5, 6}     # サイコロの目のsetを定義
even = {2, 4, 6, 8, 10}     # 偶数のsetを定義

odd_dice = dice - even     # サイコロの目と偶数の差集合を取る
print(odd_dice)     # 奇数の目だけを表示する

# setの交わりを得る
print("<setの交わりを得る>")
prefs = {"北海道", "青森", "秋田", "岩手"}     # 県名のsetを定義
capitals = {"札幌", "青森", "秋田", "盛岡"}     # 県庁所在地のsetを定義

pref_cap = prefs & capitals     # 2つの交わりを得る
print(pref_cap)

# setの対称差を得る
print("<setの対称差を得る>") 
prefs = {"北海道", "青森", "秋田", "岩手"}     # 県名のsetを定義
capitals = {"札幌", "青森", "秋田 ", "盛岡"}     # 県庁所在地のsetを定義

pref_cap2 = prefs ^ capitals     # 2つの対称差を得る
print(pref_cap2)

# setとリスト
print("<setとリスト>")
codon = ['ATG', 'GGC', 'TCC', 'AAG', 'TTC', 'TGG', 'GAG', 'TCC']     # 文字列のリスト
s_codon = set(codon)     # リストをsetに変換
print(len(codon), len(s_codon))     # リストとsetの長さを表示

# setと比較
print("<setと比較>")
prime = {2, 3, 5, 7, 13, 17}     # 素数のsetを定義
fib = {1, 1, 2, 3, 5, 8, 13}     # フィボナッチ数のsetを定義

prime_fib = prime & fib     # 2つの交わりを得る
if 13 in prime_fib:
    print("13は素数で、フィボナッチ数でもある")
if {2, 3} <= prime_fib:
    print("2, 3は素数で、フィボナッチ数でもある")