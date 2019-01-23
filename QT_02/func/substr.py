"""startからlenで指定された文字数分のみ切り出す"""
import re

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """

    if param is None:
        raise SyntaxError("引数がありません")

    pattern = re.compile(r'([0-9]+),([0-9]+)')
    plist = pattern.findall(param)

    paramnum = len(plist)
    if paramnum != 1:
        raise SyntaxError("引数に過不足があります")

    paramnum = len(plist[0])
    if paramnum != 2:
        raise SyntaxError("引数に過不足があります")

    startpos = int(plist[0][0])
    cutlen = int(plist[0][1])

    # 開始位置が０以下、切り出す長さが負
    if startpos < 1 or cutlen < 0:
        raise SyntaxError("引数の値が不正です")

    # main_funcで演算せずに使えるよう以下の形で返す
    # 切り出し開始位置(添え字),切り出し終了位置(添え字)
    cutlen = startpos + cutlen -1
    startpos -= 1

    func_data = (startpos, cutlen)
    return func_data

def main_func(num, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""

    # dataの長さと、切り出す開始位置、終了位置を確認
    datalen = len(data)
    if num[0] + 1 > datalen:
        raise ValueError("切り出し開始位置がデータ長に対して不正です")
    if num[1] + 1 > datalen:
        raise ValueError("切り出し終了位置がデータ長に対して不正です")

    data = data[num[0]:num[1]]

    return data

def main():
    """main"""

if __name__ == '__main__':
    main()
