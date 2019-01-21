"""前後の空白文字列(スペース、タブ、改行)をカットする"""

def init_func(param):
    """ paramは各関数に渡す引数。ここで初期処理を行う """

    if param is not None:
        raise SyntaxError("不要な引数があります")
    func_data = None

    return func_data

def main_func(func_data, data):
    """ dataは処理対象とする入力データ。func_dataはinit_funcの戻り値 ここで実際の変換処理を行う"""

    if func_data is not None:
        raise SyntaxError("不要な引数があります")   # Pylint 10点のために追加したが...

    data = data.strip()

    # このデータが変換後のデータとして出力される(もしくは次の変換の入力データになる)
    return data

def main():
    """main"""

if __name__ == '__main__':
    main()
