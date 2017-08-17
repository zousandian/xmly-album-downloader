#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import DownloaderClass
try:
      import readline
except ImportError:
      import pyreadline as readline

# 解决打包成exe执行时无法粘贴的问题
readline.parse_and_bind("control-v:paste")

# https://github.com/pyinstaller/pyinstaller/issues/1240#issuecomment-95360443
print '\n\n=========喜马拉雅专辑下载========\n\n'.decode('utf-8')
def waitAlbumUrl():
    msg = u'请输入专辑链接,回车键继续(例子：http://www.ximalaya.com/6749726/album/5289107/): \n'
    albumUrl = raw_input(msg.encode(sys.stdin.encoding)).decode(sys.stdin.encoding)
    return albumUrl

def waitDist():
    msg = u'请输入文件保存路径,回车键继续(默认在系统【下载/Downloads】目录): \n'
    dist = raw_input(msg.encode(sys.stdin.encoding)).decode(sys.stdin.encoding)
    return dist

albumUrl = len(sys.argv) > 1 and sys.argv[1] or waitAlbumUrl()
dist = len(sys.argv) > 2 and sys.argv[2] or waitDist()
DownloaderClass.Downloader(albumUrl, dist)