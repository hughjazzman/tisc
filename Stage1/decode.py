#!/usr/bin/env python3
import sys
import subprocess
import bz2
import zlib
import lzma
import base64
import codecs
import gzip

filename = "tempcopy3"


def yes():
    counter = 1
    while True:
        sub = subprocess.Popen("file -b " + filename + "| awk '{print $1}'", shell=True, stdout=subprocess.PIPE)

        sub_rtn = sub.stdout.read().decode().strip()

        f = open(filename, 'rb')
        ans = f.read()
        f.close()
        if sub_rtn == "bzip2":
            ans = bz2.decompress(ans)
        elif sub_rtn == "ASCII":
            sub = subprocess.Popen("file -b " + filename + "| awk '{print $NF}'", shell=True, stdout=subprocess.PIPE)
            last = sub.stdout.read().decode().strip()
            if last == "terminators":
                ans = codecs.decode(ans, "hex")
            else:
                ans = base64.decodebytes(ans)
        elif sub_rtn == "XZ":
            ans = lzma.open(filename).read()
        elif sub_rtn == "zlib":
            ans = zlib.decompress(ans)
        elif sub_rtn == "gzip":
            f = gzip.open(filename, 'rb')
            ans = f.read()
            f.close()
        else:
            break
        f = open(filename, 'wb')
        f.write(ans)
        f.close()
        counter += 1
        sys.stdout.write("Counter " + str(counter) + ", " + sub_rtn + "\n")
        

if __name__ == "__main__":
    yes()