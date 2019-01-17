"""sample"""
import csv
import os
import re
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


def read_conf(conffname):
    """クレンジング設定ファイルを読む"""
    with open(conffname, 'rt', encoding='utf-8') as inf:
        rd = csv.reader(inf)
        data = sorted(rd, key=lambda x: (x[0])) # 項目番号でソート(不要？)
    return(data)

def read_data(infname):
    """入力データ(csv)を読む"""
    with open(infname, 'rt', encoding='utf-8') as inf:
        rd = csv.reader(inf)
        # 入力ファイルを1行ずつ読んでリストを返す
        for line in rd:
            yield line

def cleansing_data(infname, conffname):
    """入力データに従い、クレンジング処理を実行する"""
    # クレンジング設定ファイルを読む
    conflist = read_conf(conffname)

    # 入力データを1行ずつ読みながら、クレンジング
    for data in read_data(infname):
        for col,funcname, parm in conflist:
            colno = int(col)
            print("BASE : ",colno,funcname, "parm = ", parm, "data = ", data[colno-1])

            # カッコ悪いけど毎回ロードする(クレンジング設定のように事前に持っておきたいけど)
            m = importlib.import_module("func."+funcname)
            ret = m.init_func(parm)
            data[colno-1] = m.main_func(ret, data[colno-1])
            print("BASE : data = ", data[colno-1])
        yield data

def write_data(infname, conffname, outfname):
    """クレンジング後のデータをCSVファイルに出力する"""
    with open(outfname, 'wt', encoding='utf-8', newline='') as outf:
        csvwriter = csv.writer(outf)
        csvwriter.writerows(cleansing_data(infname, conffname))

def main(argv):
    """main（引数チェックはパクリ）"""
    result = 1

    try:
        # # 引数チェック
        # args = parse_args(argv)
        # # 入力データに基づき変換処理を呼び出す
        # write_data(args['-i'], args['-f'], args['-o'])

        #テスト用
        # ifile = r"C:\kitazawa\dev\python_training\QT_02\sample.in"
        # ffile = r"C:\kitazawa\dev\python_training\QT_02\sample.conf"
        # ofile = r"C:\kitazawa\dev\python_training\QT_02\out.txt"
        ifile = r"D:\kitaz\Python_Training\QT_02\sample.in"
        ffile = r"D:\kitaz\Python_Training\QT_02\sample2.conf"
        ofile = r"D:\kitaz\Python_Training\QT_02\out.txt"
        write_data(ifile, ffile, ofile)
#        cleansing_data(ifile, ffile, ofile)

    except (ArgsError, MemoryError, OSError) as exc:
        print(exc, file=sys.stderr)

    except ValueError as exc:
        print(exc)

    except SyntaxError as exc:
        print("例外が発生しました。行数()　項目番号()")
        print(exc)

        # basic_11 を参考に例外処理

    else:
        result = 0
    return result

if __name__ == '__main__':
#    sys.exit(main(sys.argv))
    (main(sys.argv))
