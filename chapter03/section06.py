# 06_関数の応用
print(int("101010", 2))     # 2進数相当の文字列を数値に変換

# 関数にデフォルト引数を定義する
print("<関数にデフォルト引数を定義する>")
'''
関数にデフォルト引数を定義する記法
def 関数名(引数1=デフォルト値, 引数2=デフォルト値):
    関数のブロック
'''
def fizzbuzz(count=100, fizzmod=3, buzzmod=5):
    for cnt in range(1, count+1):     # count回繰り返し
        if cnt%fizzmod == 0 and cnt%buzzmod == 0:     # fizzmodでもbuzzmodでも割り切れる
            print("FizzBuzz")
        elif cnt%fizzmod == 0:     # fizzmodで割り切れる
            print("Fizz")
        elif cnt%buzzmod == 0:     # buzzmodで割り切れる
            print("Buzz")
        else:
            print(cnt)     # 数値を表示する
fizzbuzz()

# 引数のキーワード指定
print("<引数のキーワード指定>")
# print(int(base=2, x="1010"))     # ←動かない

# 関数とローカル変数
print("<関数とローカル変数>")
local_var = 1     # 関数の外で変数を定義

def test_func(an_arg):
    local_var = an_arg     # 関数の中で同盟の変数を定義
    print("test_func()の中 =", local_var)

test_func(200)
print("test_func()の外 =", local_var)
