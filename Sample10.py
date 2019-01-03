#decorator
def deco(func):
    print("wrapper before deco IN ：")
    def wrapper(x):
        print("wrapper IN 直後：", x)
        wx = "---" + x + "---"
        return func(wx)
    print("wrapper OUT deco IN ：")
    return wrapper

@deco
def printmsg(x1):
    print(x1, "を入力しました。")

str = input("メッセージを入力してください。")

printmsg(str)
