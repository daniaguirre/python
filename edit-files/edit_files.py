import os

template = 'example'

f = open('example', 'w')

f.writelines(['_RWS := rec(\n',\
              'isRWS := true,'])

f.close()
os.c
os.rename('example', 'example1')