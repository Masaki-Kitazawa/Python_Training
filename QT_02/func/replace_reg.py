"""サンプル"""

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """
    print("in init_func　：", __name__)
    func_data = "FUNC_DATA"
    return func_data #各プラグイン固有データ。main_funcの第一引数で使用される

def main_func(func_data, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""
    print("in main_func　：", __name__)
    data = "replace"
    # このデータが変換後のデータとして出力される(もしくは次の変換の入力データになる)
    return data

def main():
    pass

if __name__ == '__main__':
    main()
