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


def read_conf(conffname):
    """クレンジング設定ファイルを読み、リストにして返す（リスト　1:項目番号、2:プラグインへの引数、3:モジュール）"""
    with open(conffname, 'rt', encoding='utf-8') as inf:
        csvrd = csv.reader(inf)
        data = []

        for row in csvrd:
            rownum = len(row)

            # クレンジング設定ファイルは、2項目or③項目のはず
            if rownum not in (2, 3):
                raise SyntaxError("クレンジング設定ファイルの記載が不正です")

            col = row[0]
            funcname = row[1]
            # ,があって、何等か文字列がある場合は引数
            if rownum == 3 and row[2] != '':
                param = row[2]
            # ,がない、空文字の場合はプラグインへの引数無し
            else:
                param = None

            # プラグインを読み込む
            plugmod = importlib.import_module("func."+funcname)
            # プラグインのinit_funcが正常終了時は、クレンジング設定のリストに追加
            data.append([col, plugmod.init_func(param), plugmod])

    return data

def read_data(infname):
    """入力データ(csv)を読む"""
    with open(infname, 'rt', encoding='utf-8') as inf:
        csvrd = csv.reader(inf)
        # 入力ファイルを1行ずつ読んでリストを返す
        for line in csvrd:
            yield line

def cleansing_data(infname, conffname):
    """入力データに従い、クレンジング処理を実行する"""
    # クレンジング設定ファイルを読む
    conflist = read_conf(conffname)

    # 入力データを1行ずつ読みながら、クレンジング
    lineno = 0
    for data in read_data(infname):
        lineno += 1
#        for col, funcname, param, plugmod in conflist:
        for col, param, plugmod in conflist:
            colno = int(col)

            try:
                # プラグインのmain_funcを呼ぶ
                data[colno-1] = plugmod.main_func(param, data[colno-1])
            except (ValueError, SyntaxError) as exc:
                print("例外が発生しました。行数(", lineno, ")　項目番号(", colno, ")")
                print("理由:", exc)
                print("データ:", data[colno-1])
                sys.exit()
            else:
                pass

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
