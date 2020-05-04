str= 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!'

a= " ".join(str.split())
b= a.replace(':',',')
c=" ".join(b.split())
d=c.replace('naMe','name')
e=d.replace('my','My')

print((e.rstrip('!!!!!!'))+'.')