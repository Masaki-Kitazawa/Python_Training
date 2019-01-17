"""サンプル"""
import re

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """

    # 文字列をカンマで分割する
    # 1個目は正規表現、2個目以降は置換する正規表現
    # 2個目以降を,で結合する
    tmp = param.split(',')
    if len(tmp) < 2:
        print("引数足りないエラー")
    else:
        ptnkey = tmp[0]
        repkey = tmp[1]
        for hoge in tmp[2:len(tmp)]:
            repkey += "," + hoge

#    repkey = "\\1,\\2,\\3"

    # pattern = re.compile(r'(.*),(.*)')
    # for ptnkey, repkey in pattern.findall(param):
    #     print(ptnkey, repkey)

    func_data = [ptnkey, repkey]

    return func_data


def main_func(func_data, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""

#    pattern = re.compile(func_data[0])
#    pattern = re.compile(r'(\d+)-(\d+)-(\d+)')

    print(__name__, "(B) ：", data)

#    data = re.sub(r'(.)(.)(.)$', r'\1,\2,\3', data)

    data = re.sub(func_data[0], func_data[1], data)

    print(__name__, "(A) ：", data)



    # このデータが変換後のデータとして出力される(もしくは次の変換の入力データになる)
    return data

def main():
    pass

if __name__ == '__main__':
    main()
