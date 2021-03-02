# 05_ループの応用
# while文でループを作る
print("<while文でループを作る>")
'''
while文の記法
while 条件式:
    ループ内で実行するブロック
'''
cnt = 1     # ループカウンタを初期化
while cnt <= 100:     # 1から100まで繰り返し
    if cnt%3 == 0 and cnt%5 == 0:     # 3で割り切れ、かつ5でも割り切れる
        print("FizzBuzz")
    elif cnt%3 == 0:     # 3で割り切れる
        print("Fizz")
    elif cnt%5 == 0:     # 5で割り切れる
        print("Buzz")
    else:
        print(cnt)     # 数値を表示する
    cnt = cnt+1     # カウンタを1増やす

# break文とcontinue文を使ったループの制御
print("<break文とcontinue文を使ったループの制御>")
from random import randint     # 乱数を作る関数を読み込み
hands = {0:"グー", 1:"チョキ", 2:"バー"}     # じゃんけんの手
rules = {(0, 0):"あいこ", (0 ,1):"勝ち", (0, 2):"負け",     # 勝ち負けのルール
         (1, 0):"負け", (1, 1):"あいこ", (1, 2):"勝ち",
         (2, 0):"勝ち", (2, 1):"負け", (2, 2):"あいこ" }

while True:     # じゃんけんのループ
    pc_hand = randint(0, 2)     # 乱数で手を決める
    user_hand_str = input("0:グー 1:チョキ 2:パー 3:やめる")
    if user_hand_str == "3":     # 終了の数値が入力されたのでループを抜ける
        break
    if user_hand_str not in ("0", "1", "2"):     # 不正な入力の場合、ループの先端に戻る
        continue
    user_hand = int(user_hand_str)     # ユーザの手を数値に変換
    print("あなた"+hands[user_hand]+"、コンピュータ:"+hands[pc_hand])     # 手を表示する

    print(rules[(user_hand, pc_hand)])

# ループのelse
print("<ループのelse>")
a_num = 59     # 素数かどうかを調べる数
for num in range(2, a_num):     # 2からa_num-1まで繰り返す
    if a_num % num == 0:     # a_numをnumで割り切れるか
        print(a_num, "は素数ではありません")
        break
else:
    print(a_num, "は素数です")     # break文を一度も通らないでループが終了した
