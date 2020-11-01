import bz2
import zlib
import lzma
import base64
import codecs

f = open('temp.mess', 'rb')
s = f.read()
f.close()
ans = bz2.decompress(s)
ans = zlib.decompress(ans)



f = open('temp2', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp2').read()
ans = zlib.decompress(ans)
ans = base64.decodebytes(ans)
##ans = codecs.decode(ans, "hex")
##ans = base64.decodebytes(ans)
##
f = open('temp3', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp3').read()
ans = codecs.decode(ans, "hex")
ans = zlib.decompress(ans)
ans = codecs.decode(ans, "hex")
ans = base64.decodebytes(ans)

f = open('temp4', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp4').read()

f = open('temp5', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp5').read()
ans = codecs.decode(ans, "hex")
ans = zlib.decompress(ans)
ans = codecs.decode(ans, "hex")


f = open('temp6', 'wb')
f.write(ans)
f.close()

import gzip

f = gzip.open('temp6', 'rb')
ans = f.read()
f.close()
f = open('temp7', 'wb')
f.write(ans)
f.close()

f = gzip.open('temp7', 'rb')
ans = f.read()
f.close()
f = open('temp8', 'wb')
f.write(ans)
f.close()

ans = codecs.decode(ans, "hex")
ans = bz2.decompress(ans)

f = open('temp9', 'wb')
f.write(ans)
f.close()

f = gzip.open('temp9', 'rb')
ans = f.read()
f.close()
f = open('temp10', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp10').read()

f = open('temp11', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp11').read()
ans = base64.decodebytes(ans)

f = open('temp12', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp12').read()
ans = base64.decodebytes(ans)
ans = codecs.decode(ans, "hex")
ans = bz2.decompress(ans)
ans = codecs.decode(ans, "hex")

f = open('temp13', 'wb')
f.write(ans)
f.close()

f = gzip.open('temp13', 'rb')
ans = f.read()
f.close()
f = open('temp14', 'wb')
f.write(ans)
f.close()
f = gzip.open('temp14', 'rb')
ans = f.read()
f.close()

ans = codecs.decode(ans, "hex")

f = open('temp15', 'wb')
f.write(ans)
f.close()

ans = lzma.open('temp15').read()
ans = codecs.decode(ans, "hex")
ans = base64.decodebytes(ans)
ans = base64.decodebytes(ans)
ans = bz2.decompress(ans)

f = open('temp16', 'wb')
f.write(ans)
f.close()
