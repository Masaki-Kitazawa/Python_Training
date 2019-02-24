"""データクレンジング簡易ツールのベース部分"""
import csv
import os
import sys
import importlib

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




def main(argv):
    """main（引数チェックはパクリ）"""
    result = 1

    try:
        # 本番用
        # 引数チェック
        args = parse_args(argv)
        # 入力データに基づき変換処理を呼び出す
        write_data(args['-i'], args['-f'], args['-o'])

        #テスト用
        # ifile = r"C:\kitazawa\dev\python_training\QT_02\sample.in"
        # ffile = r"C:\kitazawa\dev\python_training\QT_02\sample.conf"
        # ofile = r"C:\kitazawa\dev\python_training\QT_02\out.txt"
        # ifile = r"D:\kitaz\Python_Training\QT_02\sample.in"
        # ffile = r"D:\kitaz\Python_Training\QT_02\sample.conf"
        # ofile = r"D:\kitaz\Python_Training\QT_02\out.txt"
        # write_data(ifile, ffile, ofile)

    except (ArgsError, MemoryError, OSError) as exc:
        print(exc, file=sys.stderr)

    else:
        result = 0
    finally:
        pass

    return result

if __name__ == '__main__':
#    sys.exit(main(sys.argv))
    (main(sys.argv))
