import os
import MySQLdb
import smtplib
import random
import string
from datetime import datetime
from flask import Flask, session, url_for, redirect, render_template, request, abort, flash, send_file
from database import db_connect,inc_reg,ins_loginact,vr1,upload_act,download_act

import io
import json


# def db_connect():
#     _conn = MySQLdb.connect(host="localhost", user="root",
#                             passwd="root", db="assigndb")
#     c = _conn.cursor()

#     return c, _conn



app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route("/user.html")
def ins():
    return render_template("user.html")

@app.route("/ihome.html")
def ihome():
    return render_template("ihome.html")


@app.route("/increg.html")
def increg():
    return render_template("increg.html")

@app.route("/ap3.html")
def ap3():
    return render_template("ap3.html")

@app.route("/vr.html")
def vr():
    return render_template("vr.html")

@app.route("/index")
def index1():
    return render_template("index.html")




@app.route("/send",methods = ['GET','POST'])
def send():
    username = session['username']
    branch = request.form['branch']
    data = vr1(branch)
    print(data)
    return render_template("vr1.html",data=data)


@app.route("/download", methods = ['GET','POST'])
def download():
    
    id = request.args.get('id')
    fname = download_act(id)
    fname = fname[0][0]
    print(fname)
    # data1 = data[0][9]
    # data2 = data[0][9]
    # print("------------------------")
    # print(data[0][7])
    # fname = "download.pdf"
    # file_stream = io.BytesIO(filedata[0][0])
    # return send_file(
    #             file_stream,
    #             attachment_filename=fname,
    #             as_attachment=True
    #         )
    return send_file('C:/Users/Sai Deekshitha/Notesshala/static/'+fname , as_attachment=True, attachment_filename=fname )

# -------------------------------Registration-----------------------------------------------------------------    



@app.route("/inceregact", methods = ['GET','POST'])
def inceregact():
   if request.method == 'POST':    
      
      status = inc_reg(request.form['username'],request.form['password'],request.form['email'],request.form['mobile'],request.form['branch'])
      
      if status == 1:
       return render_template("user.html",m1="sucess")
      else:
       return render_template("increg.html",m1="failed")
      



   


@app.route("/upload", methods = ['GET','POST'])
def upload():
   if request.method == 'POST':    
      
      username = session['username']
      branch =request.form['branch']
      about =request.form['about']
      file = request.files['pdf_file']
      fname = file.filename
      file_data =  file.read()
      paragraph_string = file_data[0]
      print("88888888888888888888888888888888888")
      print(paragraph_string)
      print("9999999999999999")
     
      status = upload_act(username,branch,about,fname)
      
      if status == 1:
       return render_template("ap3.html",m1="sucess")
      else:
       return render_template("ap3.html",m1="failed")



@app.route("/inslogin", methods=['GET', 'POST'])       
def inslogin():
    if request.method == 'POST':
        status = ins_loginact(request.form['username'], request.form['password'])
        print(status)
        if status == 1:
            session['username'] = request.form['username']
            return render_template("ihome.html", m1="sucess")
        else:
            return render_template("inc.html", m1="Login Failed")
        



# # -------------------------------Loginact End-----------------------------------------------------------------


   
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
