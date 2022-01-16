import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS korzina(
TG_ID INTEGER ,
ZAKAZ STRING,
COST INTEGER, 
KOLICH INTEGER
)''')
first_insert2 = '''
INSERT INTO korzina VALUES ('{}','{}','{}', ' ' )
'''
tg_id_upd = '''
UPDATE korzina
SET TG_ID = '{}'
WHERE TG_ID = '{}'
'''
tg_id_select = '''
SELECT TG_ID
FROM korzina
WHERE TG_ID = '{}'
'''

zakaz_upd = '''
UPDATE korzina
SET ZAKAZ = '{}'
WHERE TG_ID = '{}'
'''
zakaz_select = '''
SELECT ZAKAZ
FROM korzina
WHERE TG_ID = '{}'
'''

kolich_upd = '''
UPDATE korzina
SET KOLICH = '{}'
WHERE TG_ID = '{}'
and ZAKAZ ='{}'
'''
kolich_select = '''
SELECT KOLICH
FROM korzina
WHERE TG_ID = '{}'
'''
