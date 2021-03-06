# 04_if文の応用
# 比較演算子
'''
Pythonの比較演算子
演算子 / 例 / ブロックを実行する条件
== / x == y / xとyが等しい
!= / x != y / xとyが異なる
> / x > y / xの方がyより大きい
< / x < y / xよりyの方が大きい
>= / x >= y / xとyが等しいかxが大きい
<= / x <= y / xとyが等しいかyが大きい
in / x in y / xという要素がy(シーケンス)に存在する
'''

# 比較演算子とTrue False
print("<比較演算子とTrue, False>")
print(1 + 1 == 2)
print(5**(4-4)+9 == 10)
print(5 > 2)
print(100 == 100.0)
print("かなこ" != "かなこぉ↑↑")
print([1, 2, 3] == [1, 2, 3])

# 複雑な比較 - 論理演算
print("<複雑な比較 - 論理演算>")
v = 30000     # 打ち出し速度(Km/h)
if v < 28400:     # 第1宇宙速度以下
    print("地上に落下します")
if v > 28400 and v < 40300:     # 第1宇宙速度以上で第2宇宙速度未満
    print("月とお友達です")
if v >= 40300 and v < 60100:     # 第2宇宙速度以上で第3宇宙速度未満
    print("惑星の仲間入りです")
if v >= 60100:
    print("アルファケンタウリを目指せ")