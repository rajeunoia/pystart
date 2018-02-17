import json
import sqlite3 as sq

admin_db_name = "bot_admin.db"
pages_table = "connected_pages"
def admin_table_exists(conn,table_name):
    result = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='"+table_name+"'")
    result_data = result.fetchall()
    if len(result_data)>0 and result_data[0][0] == table_name:
        return True
    else: 
        return False

def insert_page(page_data):
    conn = sq.connect(admin_db_name)
    if admin_table_exists(conn,pages_table):
        conn.execute('insert into connected_pages("user_id","page_id","page_name","page_token") values ("'+page_data["userid"]+'","'+page_data["pageid"]+'","'+page_data["pagename"]+'","'+page_data["pagetoken"]+'")')
    else:
        conn.execute('create table  connected_pages ("id" INTEGER PRIMARY KEY AUTOINCREMENT,"user_id" CHAR(30) NOT NULL,"page_id" CHAR(30), "page_name" CHAR(30), "page_token" CHAR(200))')
        conn.execute('insert into connected_pages("id","user_id","page_id","page_name","page_token") values (1,"'+page_data["userid"]+'","'+page_data["pageid"]+'","'+page_data["pagename"]+'","'+page_data["pagetoken"]+'")')
    conn.commit()    
    conn.close()
    

def print_pages():
    conn = sq.connect(admin_db_name)
    pages = ""
    if admin_table_exists(conn,pages_table):
        result = conn.execute('select * from '+pages_table)
        pages = result.fetchall()
        print(pages)
    conn.close()
    return str(pages)


def get_token_for_page(page_id):
    conn = sq.connect(admin_db_name)
    pages = ""
    token = None
    if admin_table_exists(conn,pages_table):
        result = conn.execute("select * from "+pages_table +" where page_id == '"+page_id+"'")
        pages = result.fetchall()
        print(pages)
    if len(pages) > 0:
        token = page[0][4]
    conn.close()
    return token
    
