# 09_関数と組み込み型
'''
def foo():
    return [valuea, valueb]
alist = foo()
'''

# 戻り値とアンパック代入
'''
def bar(seq):
    return [minvalue, maxvalue, average]
    # return minvalue, maxvalue, average
minvalue, maxvalue, average = bar(seq)
'''

# 関数で引数リストを受け取る
def foo(a, b, *vals):     # *引数を持つ関数を定義
    print(a, b, vals)

foo(1, 2, 3, 4, 5)     # 5つの数値を引数に指定して呼び出し
# print(foo(1, 2, c=3))     # cという未定義のキーワード引数を指定
'''
Traceback (most recent call last):
  File "section09.py", line 21, in <module>
    print(foo(1, 2, c=3))
TypeError: foo() got an unexpected keyword argument 'c'
'''

# 関数でキーワード引数を受け取る
def bar(a, b, **args):     # **引数を持つ関数を定義
    print(a, b, args)

bar(1, 2, c=3, d=4)     # 未定義のキーワード引数を指定
