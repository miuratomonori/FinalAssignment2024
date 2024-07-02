import os
import logging
import datetime as dt

#現在時刻の取得
now = dt.datetime.now()
now = now.strftime('%Y-%m-%d %H-%M-%S-%f')

#ファイルのパスと名前の指定
path = '.\\Section04\\log\\'+str(now)+'.log'
#新規ファイルの作成
log = open(path,'w')

log.write('This is test. File launch successful' + str(now))
log.close()