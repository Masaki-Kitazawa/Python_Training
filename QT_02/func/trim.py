"""前後の空白文字列(スペース、タブ、改行)をカットする"""

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """
    if (param != ""):
        print(__name__, "パラメータは不要なのだが")
    func_data = ""
    return func_data

def main_func(func_data, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""
    print(__name__, "(B) ：", data)
    data = data.strip()
    print(__name__, "(A) ：", data)

    # このデータが変換後のデータとして出力される(もしくは次の変換の入力データになる)
    return data

def main():
    pass

if __name__ == '__main__':
    main()
