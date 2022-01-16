import sqlite3
conn = sqlite3.connect('b_users.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Menyu(
TOVAR_UZ STRING,
TOVAR_RU STRING,
PRICE INTEGER 
)''')
first_insert3 = '''
INSERT INTO Menyu VALUES ('{}','{}','{}')
'''
tovar_upd = '''
UPDATE Menyu
SET {} = '{}'
WHERE TOVAR_RU = '{}'
'''
tovar_select = '''
SELECT {}
FROM korzina
WHERE {} = '{}'
'''



price_upd = '''
UPDATE Menyu
SET PRICE = '{}'
WHERE TOVAR = '{}'
'''
price_select = '''
SELECT PRICE
FROM Menyu
WHERE {} = '{}'
'''