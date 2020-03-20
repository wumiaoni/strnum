"""
手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。
如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，
以此规则试设计一个程序，将单词用一串数字来进行表示。
举例
输入：cat（不区分大小写）
输出：228
"""

def strnum(instr):
    dit = {'abcABC': '2',
           'defDEF': '3',
           'ghiGHI': '4',
           'jklJKL': '5',
           'mnoMNO': '6',
           'pqrsPQRS': '7',
           'tuvTUV': '8',
           'wxyzWXYZ': '9'
           }
    num = ''
    for i in instr:
        for key, values in dit.items():
            if i in key:
                num += values
    return int(num)


if __name__ == '__main__':
    instr = input("请输入字母：")
    n = strnum(instr)
    print(n)
