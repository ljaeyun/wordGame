import sqlite3
import datetime
import time
import random
import winsound


conn = sqlite3.connect('data/record.db', isolation_level=None)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS record
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cor_cnt INTEGER,
        record text,
        regdate text
    )
""")

curtime = datetime.datetime.now().strftime('%Y- %m-%d %H:%M:%S')

words = []

n = 1
cor_cnt = 0

with open('./resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

print(words)

input('press enter key')

start = time.time()  # time stamp 값

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)


    print()

    print("*Question # {}".format(n))
    print(q)

    x = input()
    n += 1
    print()

    if str(q).strip() == str(x).strip():
        # winsound.PlaySound(
        #     './sound/good.wav',
        #     winsound.SND_FILENAME
        # )
        cor_cnt += 1
        print("pass")

    else:
        # winsound.PlaySound(
        #     '/sound/bad.wav',
        #     winsound.SND_FILENAME
        # )
        print("wrong")



end = time.time()

et = end - start

et = format(et, '.3f')
print()
print('='*20)

if cor_cnt >= 3:
    print("결과 : 합격")
else:
    print('불합격')

sql1 = """INSERT INTO record
(cor_cnt, record, regdate) 
VALUES (?, ?, ?)"""

cursor.execute(sql1,(cor_cnt, et, curtime))

conn.close()

print(et, cor_cnt)