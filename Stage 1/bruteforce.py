#!/usr/bin/env python3

from zipfile import ZipFile

for i in range(16777216,0,-1):
    try:
        p = hex(i)[2:]
        p="".join(('0'*(6-len(p)),p))
        with ZipFile('5b5a48faae9d04594f76adbb3f7177a9.zip', 'r') as myzip:
            myzip.extractall(pwd=p.encode())
        
    except Exception as e:
        msg = str(e)[:3]
        if (msg != "Bad" and msg != "Err"):
            print(e)
            print(p)
            
        continue
    else:
        print("Password found:" + p)

