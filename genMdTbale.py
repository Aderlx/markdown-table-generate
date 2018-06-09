#!/usr/bin/env python
# coding:utf-8
u"""
Usage:
  genMdTable.py [options] <filename>
  genMdTable.py [options] <filename> [-o] <outfile>
  genMdTable.py <filename> [-o] <outfile>
  genMdTable.py (-v|--version)
  genMdTable.py (-h|--help)

Options:
  -h --help      帮助
  -v --version   显示版本号.
  -r --right     markdown文档，右对齐
  -l --left      markdown文档，左对齐
  -c --center    markdown文档，居中(默认)
  -o --outfile   输出文件(默认打印终端上)
"""

from docopt import docopt
import csv

__version__ = "0.1.1"


class rfile(object):
    """
    read csv file.
    """

    def __init__(self, filename):
        self.filename = filename

    def rfile(self):
        csvfile = open(self.filename, 'r')
        reader = csv.reader(csvfile)
        content = [line for line in reader]
        csvfile.close()
        return content


class generateTable(object):
    """
    generate makedown table format.
    """
    AlignRight = '| ---: '
    AlignLeft = '| :--- '
    Centered = '| :---: '

    def __init__(self, content, align):
        self.content = content
        self.align = align
        self.num = len(content[0])


    def replaceShu(self,s):
        """
        去掉 字符串中的 |
        :return:
        str
        """
        return s.replace('|', '&#124;')

    def genHeader(self):
        if self.align == 'r':
            s = self.AlignRight * self.num + '|'
        elif self.align == 'l':
            s = self.AlignLeft * self.num + '|'
        else:
            s = self.Centered * self.num + '|'

        return s

    def genBody(self):
        contentList = ['| ' + '| '.join([self.replaceShu(i) for i in c]) + ' |' for c in self.content]
        return contentList

    def getTableList(self):
        body = self.genBody()
        header = self.genHeader()
        body.insert(1, header)
        return body


def version():
    return "version:" + __version__


def showTerminal(content):
    for line in content:
        print(line)


def saveFile(content, fname):
    with open(fname, 'w')as f:
        for line in content:
            f.write(line)
            f.write('\n')


def showTable(filename, align, is_outfile=False, outfile=None):
    obj = rfile(filename)
    content = obj.rfile()
    genTable = generateTable(content, align)
    tableList = genTable.getTableList()
    if is_outfile == False:
        showTerminal(tableList)
    else:
        saveFile(tableList, outfile)


def main():
    args = docopt(__doc__)

    if args.get("-h") or args.get("--help"):
        print(__doc__)
    elif args.get("-v") or args.get("--version"):
        print(version())

    elif args.get("-r") or args.get("--right"):
        if args.get("-o") or args.get("--outfile"):
            showTable(args.get("<filename>"), 'r', is_outfile=True, outfile=args.get("<outfile>"))
        else:
            showTable(args.get("<filename>"), 'r', is_outfile=False)

    elif args.get("-l") or args.get("--left"):
        if args.get("-o") or args.get("--outfile"):
            showTable(args.get("<filename>"), 'l', is_outfile=True, outfile=args.get("<outfile>"))
        else:
            showTable(args.get("<filename>"), 'l', is_outfile=False)

    elif args.get("-c") or args.get("--center"):
        if args.get("-o") or args.get("--outfile"):
            showTable(args.get("<filename>"), 'c', is_outfile=True, outfile=args.get("<outfile>"))
        else:
            showTable(args.get("<filename>"), 'c', is_outfile=False)

    elif args.get("<filename>"):
        if args.get("-o") or args.get("--outfile"):
            showTable(args.get("<filename>"), 'c', is_outfile=True, outfile=args.get("<outfile>"))
        else:
            showTable(args.get("<filename>"), 'c', is_outfile=False)
    else:
        print("wrong args!")
        print(__doc__)


if __name__ == '__main__':
    main()
