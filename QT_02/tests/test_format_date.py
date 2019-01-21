"""sample"""

import unittest
import func.format_date

class TestValidValues(unittest.TestCase):
    """有効値のテスト"""

    def test_valid_value0(self):
        """有効値 フォーマット無し"""
        dataset = (('', '2018/01/02 03:04:05'),)

        handle = func.format_date.init_func('')

        for expected, val in dataset:
            result = func.format_date.main_func(handle, val)
            self.assertEqual(expected, result)

    def test_valid_value1(self):
        """有効値 カンマ入りフォーマット"""
        dataset = (('A,2018,平成30,01,1,02,2,03,04,05,Z', '2018/01/02 03:04:05'),)

        handle = func.format_date.init_func('A\,YYYY\,EEYY\,MM\,mm\,DD\,dd\,HH\,MI\,SS\,Z')

        for expected, val in dataset:
            result = func.format_date.main_func(handle, val)
            self.assertEqual(expected, result)

    def test_valid_value2(self):
        """有効値 日時の境界"""

        dataset = (('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018/01/02 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018/1/2 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018/01/2 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018/1/02 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018-01-02 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018-1-2 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018-01-2 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '2018-1-02 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '平成30年01月02日 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '平成30年1月2日 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '平成30年01月2日 03:04:05'),
                   ('A 2018 平成30 01 1 02 2 03 04 05 Z', '平成30年1月02日 03:04:05'),
                   ('A 1989 平成1 01 1 08 8 00 00 00 Z', '1989/01/08'),
                   ('A 1989 昭和64 01 1 07 7 00 00 00 Z', '1989/01/07'),
                   ('A 1926 昭和1 12 12 25 25 00 00 00 Z', '1926/12/25'),
                   ('A 1926 大正15 12 12 24 24 00 00 00 Z', '1926/12/24'),
                   ('A 1912 大正1 07 7 30 30 00 00 00 Z', '1912/07/30'),
                   ('A 1912 明治45 07 7 29 29 00 00 00 Z', '1912/07/29'),
                   ('A 1900 明治33 01 1 01 1 00 00 00 Z', '1900/01/01'))

        handle = func.format_date.init_func('A YYYY EEYY MM mm DD dd HH MI SS Z')

        for expected, val in dataset:
            result = func.format_date.main_func(handle, val)
            self.assertEqual(expected, result)

class TestBadValues(unittest.TestCase):
    """無効値のテスト"""

    def test_format(self):
        """無効値 不正な日時形式"""

        dataset = ('',
                   '9/01/01',
                   '99/01/01',
                   '999/01/01',
                   '2018/012/01',
                   '2018/01/',
                   '2018//01',
                   '/01/01',
                   '//',
                   '2018-01-',
                   '2018--01',
                   '-01-01',
                   '--',
                   '平成2年01月日',
                   '平成2年月01日',
                   '平成年01月01日',
                   '昭和2年01月日',
                   '昭和2年月01日',
                   '昭和年01月01日',
                   '大正2年01月日',
                   '大正2年月01日',
                   '大正年01月01日',
                   '明治2年01月日',
                   '明治2年月01日',
                   '明治年01月01日',
                   '慶応1年9月7日 ',
                   '2018/01/01 00:00:0',
                   '2018/01/01 00:0:00',
                   '2018/01/01 0:00:00',
                   '2018/01/01 00:00:',
                   '2018/01/01 00::00',
                   '2018/01/01 :00:00',
                   '2018/01/01 ::')

        handle = func.format_date.init_func('a')

        for val in dataset:
            self.assertRaises(
                ValueError,
                func.format_date.main_func, handle, val)

    def test_date(self):
        """無効値 日時の境界"""

        dataset = ('2018/1/32',
                   '2018/2/29',
                   '2018/3/32',
                   '2018/4/31',
                   '2018/5/32',
                   '2018/6/31',
                   '2018/7/32',
                   '2018/8/32',
                   '2018/9/31',
                   '2018/10/32',
                   '2018/11/31',
                   '2018/12/32',
                   '2020/2/30',
                   '1899/12/31',
                   '平成1年01月07日 ',
                   '昭和64年01月08日 ',
                   '昭和1年12月24日 ',
                   '大正15年12月25日 ',
                   '大正1年7月29日 ',
                   '明治45年7月30日 ',
                   '明治32年12月31日 ',
                   '2018/1/1 24:00:00')

        handle = func.format_date.init_func('a')

        for val in dataset:
            self.assertRaises(
                ValueError,
                func.format_date.main_func, handle, val)

if __name__ == '__main__':
    unittest.main()
