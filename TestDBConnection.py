import cx_Oracle

dsn_tns = cx_Oracle.makedsn('', '', service_name='')
conn = cx_Oracle.connect(user='', password='', dsn=dsn_tns)

c = conn.cursor()
c.execute('select count(*) from TABLE')
for row in c:
   print(row)
conn.close()