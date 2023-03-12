import hashlib

username = 'aaa'
password = 'adminsetu'
md5 = hashlib.md5()
md5.update(password.encode('utf-8'))
str_md5 = md5.hexdigest()

print(str_md5)