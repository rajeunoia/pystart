import json
import sqlite3 as sq


def table_exists(conn,table_name):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
    result_data = result.fetchall()
    if len(result_data)>0 and result_data[0][0] == table_name:
        return True
    else: 
        return False

def insert_page(page_data):
    conn = sq.connect("bot_admin.db")
    if table_exists(conn,"connected_pages"):
        conn.execute('insert into connected_pages("user_id","page_id","page_name","page_token") values ("'+page_data["userid"]+'","'+page_data["pageid"]+'","'+page_data["pagename"]+'","'+page_data["pagetoken"]+'")')
    else:
        conn.execute('create table  connected_pages ("id" INTEGER PRIMARY KEY AUTOINCREMENT,"user_id" CHAR(30) NOT NULL,"page_id" CHAR(30), "page_name" CHAR(30), "page_token" CHAR(200))')
        conn.execute('insert into connected_pages("id","user_id","page_id","page_name","page_token") values (1,"'+page_data["userid"]+'","'+page_data["pageid"]+'","'+page_data["pagename"]+'","'+page_data["pagetoken"]+'")')
    conn.commit()    
    conn.close()
    

