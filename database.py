import sqlite3
import hashlib
import datetime
import MySQLdb
from flask import session
from flask import Flask, request, send_file
import io

def db_connect():
    _conn = MySQLdb.connect(host="localhost", user="root",
                            passwd="root", db="notes")
    c = _conn.cursor()

    return c, _conn



# -------------------------------Registration-----------------------------------------------------------------


    


def inc_reg(username,password,email,mobile,branch):
    try:
        c, conn = db_connect()
        print(username,password,email,mobile,branch)
        id="0"
        
        j = c.execute("insert into user (id,username,password,email,mobile,branch) values ('"+id +
                      "','"+username+"','"+password+"','"+email+"','"+mobile+"','"+branch+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))
    

def upload_act(username,branch,about,fname):
    try:
        c, conn = db_connect()
        print(username,branch,fname)
        id="0"
       
        j = c.execute("insert into upload (id,username,branch,about,fname) values ('"+id +
                      "','"+username+"','"+branch+"','"+about+"','"+fname+"')")
        conn.commit()
        conn.close()
        print(j)
        return j
    except Exception as e:
        print(e)
        return(str(e))



def vr1(branch):
    c, conn = db_connect()
    c.execute("select * from upload where branch='"+branch+"'  ")
    result = c.fetchall()
    conn.close()
    print("result")
    return result



def download_act(id):
    c, conn = db_connect()
    c.execute("SELECT  fname FROM upload WHERE id = '"+id+"'    ")
    result = c.fetchall()
    conn.close()
    print(result)
    return result

def ins_loginact(username, password):
    try:
        c, conn = db_connect()
        
        j = c.execute("select * from user where username='" +
                      username+"' and password='"+password+"' "  )
        c.fetchall()
        conn.close()
        return j
    except Exception as e:
        return(str(e))

if __name__ == "__main__":
    print(db_connect())
