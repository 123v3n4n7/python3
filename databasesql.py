import sqlite3 as db

c = db.connect(database="tvprogramm")

cu = c.cursor()
weekdays = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг",
            "Пятница", "Суббота"]
# try:
#     cu.execute("""
#         CREATE TABLE tv (
#             tvdate DATE,
#             tvweekday INTEGER,
#             tvchannel VARCHAR(10),
#             tvtime1 TIME,
#             tvtime2 TIME,
#             prname VARCHAR(150),
#             prgenre VARCHAR(40)
#         );
#     """)
# except db.DatabaseError as x:
#     print("Ошибка: ", x)
# c.commit()
#
# try:
#     cu.execute("""
#         CREATE TABLE wd (
#             weekday INTEGER,
#             wdname VARCHAR(11)
#         );
#     """)
# except db.DatabaseError as x:
#     print("Ошибка: ", x)
# c.commit()

cu.execute("""DELETE FROM wd;""")
x = enumerate(weekdays)
b = [i for i in x]
print(b[0])
com = """INSERT INTO wd VALUES {};""".format(b[0])
print(com)
#cu.execute(com)
cu.executemany("""INSERT INTO wd VALUES (?, ?);""", enumerate(weekdays))
c.commit()
cu.close()
