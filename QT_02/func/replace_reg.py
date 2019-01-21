"""入力データに対し正規表現による置換を行う"""
import re

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """

    if param is None:
        raise SyntaxError("引数がありません")

    # 文字列をカンマで分割する
    # 1個目は正規表現、2個目以降は置換する正規表現
    # 2個目以降を,で結合する
    tmp = param.split(',')
    if len(tmp) < 2:
        raise SyntaxError("引数が足りません")
    else:
        ptnkey = tmp[0]
        repkey = tmp[1]

        # tmpが2以上に分割された場合は置換用文字列に「,」が含まれているということ
        #　この場合、エスケープされている前提のため、「,」の前に付加された「\\」を除去する
        for hoge in tmp[2:len(tmp)]:
            # ここでrepkey末尾の\\を除去する
            repkey = repkey.rstrip('\\')
            repkey += "," + hoge

    func_data = [ptnkey, repkey]

    return func_data


def main_func(func_data, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""

    data = re.sub(func_data[0], func_data[1], data)

    # このデータが変換後のデータとして出力される(もしくは次の変換の入力データになる)
    return data

def main():
    """main"""

if __name__ == '__main__':
    main()
