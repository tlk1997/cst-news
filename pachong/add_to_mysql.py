import pymysql
def add_info(title,t,url,idx):
    conn = pymysql.connect(host='host', port=3306,user = "user",passwd = "passwd",db = "database")
    sql = "insert into news value('" + title + "'," + str(t) + ",'" + url + "'," + str(idx) + ")"
    print(sql)
    cursor=conn.cursor()
    cursor.execute(sql)
    cursor.close()
    conn.commit()
    conn.close()

