"""データクレンジング簡易ツールのベース部分"""
import csv
import os
import sys
import importlib
import pandas as pd

class ArgsError(Exception):
    """arguments exception（パクリ）"""
    def __init__(self, modname, err):
        """__init__"""
        super().__init__(
            f'usage: {os.path.basename(modname)} -i INFILE -f CONFFILE -o OUTFILE\n'
            f'error: Invalid Parameter: {err}')

def parse_args(argv):
    """parse arguments（パクリ）"""
    args = {}
    i = 1
    while i < len(argv):
        if argv[i] in ('-i', '-f', '-o'):
            if (argv[i] in args) or (i == len(argv)-1):
                raise ArgsError(argv[0], argv[i])
            args[argv[i]] = argv[i+1]
            i += 2
        else:
            raise ArgsError(argv[0], argv[i])
    if '-i' not in args:
        raise ArgsError(argv[0], '-i is required')
    if '-f' not in args:
        raise ArgsError(argv[0], '-f is required')
    if '-o' not in args:
        raise ArgsError(argv[0], '-o is required')
    return args


def get_gamedata():
    """URLから試合日ｎの情報を取得する"""

    url = 'http://www.urawa-reds.co.jp/game/'
    dfs = pd.read_html(url, header=0, index_col=0)

    # 取得テーブル数確認
    print(len(dfs))

    # 取得テーブルデータ確認
    print(dfs)

    return dfs


def main(argv):
    """main（引数チェックはパクリ）"""

    dfs = get_gamedata()

    # 結合
    # df = pd.concat(dfs)

    # 0番目のテーブルを保存（リストの番号を変更する）
    dfs[0].to_csv('result.csv')



    # try:
    #     # 本番用
    #     # 引数チェック
    #     # args = parse_args(argv)
    #     # 入力データに基づき変換処理を呼び出す
    #     # write_data(args['-i'], args['-f'], args['-o'])


    # except (ArgsError, MemoryError, OSError) as exc:
    #     print(exc, file=sys.stderr)

    # else:
    #     result = 0
    # finally:
    #     pass

    # return result

if __name__ == '__main__':
#    sys.exit(main(sys.argv))
    main(sys.argv)

