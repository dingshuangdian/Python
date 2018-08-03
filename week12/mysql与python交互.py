# Create by dingshuangdian
import pymysql

# 创建连接

conn = pymysql.connect(host='119.23.57.202', port=3306, user='uroot', passwd='(Itj>G4h)f>d', db='py')

# 创建游标
cursor = conn.cursor()

# 执行SQL,并返回收影响行数
effect_row = cursor.execute("select *from py_test")

print(cursor.fetchone())
print(cursor.fetchall())
# 往表里插入数据
data = [("siq", 23, "2018-08-02"),
        ("sd", 26, "2018-08-02"),
        ("lb", 20, "2018-08-02"),

        ]

cursor.executemany("insert into py_test(name,age,register_date)values(%s,%s,%s)", data)
# 默认开启事务，必须提交
conn.commit()
cursor.close()
conn.close()
