"""startからlenで指定された文字数分のみ切り出す"""
import re

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """

    pattern = re.compile(r'([0-9]+),([0-9]+)')
    # for stpos, lennum in pattern.findall(param):
    #     print(stpos, lennum)

    plist = pattern.findall(param)
    if len(plist) < 1 or len(plist[0]) < 1:
        raise SyntaxError("引数が足りません")
    else:
        startpos = plist[0][0]
        lennum = plist[0][1]

    func_data = (int(startpos),int(lennum))
    return func_data

def main_func(num, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""

    # dataの長さと、切り出す開始位置、長さが許容範囲か確認
    datalen = len(data)
    if num[0] < 0 or num[0] > datalen:
        raise ValueError("データ長または切り出し開始位置が不正です")
    if (num[0]+num[1]-1) > datalen:
        raise ValueError("データ長または切り出し長さが不正です")

    print(__name__, "(B) ：", data)
    data = data[(num[0]-1):(num[0]+num[1]-1)]
    print(__name__, "(A) ：", data)

    return data

def main():
    pass

if __name__ == '__main__':
    main()
