"""sample"""
import csv
import os
import re
import sys

class ArgsError(Exception):
    """arguments exception（パクリ）"""
    def __init__(self, modname, err):
        """__init__"""
        super().__init__(
            f'usage: {os.path.basename(modname)} -i INFILE [-o OUTFILE]\n'
            f'error: Invalid Parameter: {err}')

def parse_args(argv):
    """parse arguments（パクリ）"""
    args = {}
    i = 1
    while i < len(argv):
        if argv[i] in ('-i', '-o'):
            if (argv[i] in args) or (i == len(argv)-1):
                raise ArgsError(argv[0], argv[i])
            args[argv[i]] = argv[i+1]
            i += 2
        else:
            raise ArgsError(argv[0], argv[i])
    if '-i' not in args:
        raise ArgsError(argv[0], '-i is required')
    if '-o' not in args:
        raise ArgsError(argv[0], '-o is required')
    return args

def read_data(infname):
    """入力データファイル(csv)を読む"""
    #yieldを使いながら、１行ずつ読む
    with open(infname, 'rt', encoding='utf-8') as inf:

        # pattern = re.compile(r'([A-Za-z][a-z\']*[a-z]|[a-z]|[A-Za-z][a-z])')
        # #入力ファイルを1行ずつ読んでリストを返す
        # for line in inf:
        #     #英小文字で始まる単語のみ
        #     yield [s for s in pattern.findall(line) if re.match('^[a-z]+', s)]

def cleansing_data():
    """入力データに従い、クレンジング処理を実行する"""
    # ループの中で、read_data
    for readlist in read_data(infname):


def main(argv):
    """main（引数チェックはパクリ）"""
    result = 1

    # 引数チェック
    args = parse_args(argv)
 
    # 入力データに基づき変換処理を呼び出す
    # cleansing_data()

    try:
        pass
        # args = parse_args(argv)
        # write_data(args['-i'], args['-o'])

        #テスト用
        # ifile = r"C:\kitazawa\dev\python_training\QT_01\sample3.txt"
        # ofile = r"C:\kitazawa\dev\python_training\QT_01\out.txt"
        # write_data(ifile, ofile)

    except (ArgsError, MemoryError, OSError) as exc:
        print(exc, file=sys.stderr)
    else:
        result = 0
    return result

if __name__ == '__main__':
#    sys.exit(main(sys.argv))
    (main(sys.argv))
