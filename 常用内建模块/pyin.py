# from datetime import datetime

# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime

# print('123')

# import base64

# t = base64.b64encode(b'binary\x00string')

# print(t)

import struct

# t = 10240099
# m = struct.pack('>I',t)

# print(m)

# s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# t = struct.unpack('<ccIIIIIIHH',s)
# print(t)

# 摘要算法-hash算法

# import hashlib

# md5 = hashlib.md5()
# md5.update('高配1'.encode('utf-8'))
# print(md5.hexdigest())

# from urllib import request

# with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

from urllib import request

req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))