
from importlib.resources import path
from unittest import result
from flask import flash, render_template, request, redirect, url_for,session,send_from_directory
from src import app
from src.models import user
from src.models import files
from src.models import acortador
from src.models.user import UsuarioModel

import os
import random
import string


from src.config import settings

from src.controllers.user import create
from src.controllers.auth import loginUser
from src.controllers.auth import nameprofile
from src.controllers.password import recoverpassword
from src.controllers.password import newpassword
from src.controllers.file import createfile
from src.controllers.file import editfile



def estaIniciado():
    return True if 'username' in session else False

@app.route("/notifi")
def noti():
        if not estaIniciado():
                print("No tiene session")
                return redirect(url_for('login'))
        return render_template("notifi/verifi-acount.html")
                      
            
@app.route("/notificacion")
def notiPassword():
        return render_template("auth/notificacionPasw.html")
        
""" @app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for("login")) """

@app.route("/logout")
def logout():
    if 'username' in session:
        session.pop('username')
        print("salir")
    return redirect(url_for("login"))




#Controllers


@app.route("/create-acount", methods =['POST','GET'])
def createUser():

        if 'username'  in session:
                return redirect(url_for('homeusr'))
    
        
        if request.method ==  'POST': 
                name=request.form.get('usuario')
                email=request.form.get('email')
                password=request.form.get('password')

                if not create.controllerCreate(name,email,password):
                        return render_template("user/crearUser.html",name=name,email=email,password=password)
                #create.controllerRegMail(name,email,password)
                notifi= True
                
                return render_template("user/crearUser.html",notifi=notifi,notifiemail=email)

        else:
                return render_template ("user/crearUser.html")

@app.get("/val-acount/<urluser>")
def validar_cuenta(urluser):
    validate_mail = request.args.get("token")
    userv = user.UserVal(validate_mail = validate_mail, vali_url=urluser)

    if not userv:
        return render_template("auth/error.html")
    else:
        user.UsuarioValidado(validate_mail = validate_mail, vali_url=urluser)

    return render_template("auth/authvalidate.html")

@app.route("/" ,methods =['POST','GET'])
def login():
        
        if 'username'  in session:
                return redirect(url_for('homeusr'))
    
        if request.method == "GET":
                return render_template("auth/login.html")
        else:
                usuario = request.form['email']
                password = request.form['password']

                if not loginUser.controllerLogin(usuario,password):
                       
                        return  render_template ("auth/login.html",usuario=usuario,password=password,session=session)

                return redirect(url_for("homeusr"))

@app.route("/recuper-password", methods =['POST','GET'])
def recuPassword():                       
        if request.method == "GET":
          return render_template("auth/recpassword.html")
        else:
                email = request.form['email']
               
                if not recoverpassword.controllerRecoverPassword(email):      
                        return render_template("auth/recpassword.html",email=email)
                return render_template("/notifi/recoverpassword.html")

@app.route("/recuper-password/<newpaswd>",methods =['POST','GET'])
def newPassword(newpaswd):

        valpassword = user.valPassword(tokenpassword=newpaswd)
        if not valpassword:
                return render_template("auth/error.html")
        if request.method == 'GET':
                return render_template("auth/newpassword.html",newpaswd=newpaswd)
        else:
                password1 = request.form.get("password1")
         
                if not newpassword.controllerNewPassword(password1,newpaswd):
                        return render_template("auth/newpassword.html",password1=password1,newpaswd=newpaswd)
                else:
                        print("Invalido")
                return render_template("/notifi/newpassword.html")



@app.route("/home", methods=['GET'])
def homeusr():
        
        if 'username' not in session:
                return redirect(url_for('login'))
        else:          
                usuario = session['username']
                naprofile = nameprofile.nameprofile()
                if request.method =="GET":
                        if 'username' not in session:
                                return redirect(url_for("login"))
                        else:
                                fils = files.listfiles(usuario)
                                return render_template("/home/home.html",fils=fils,naprofile=naprofile,usuario=usuario)
                



@app.route("/create-file",methods =['POST', 'GET'])
def createFile():

        naprofile= nameprofile.nameprofile()
        usuario = session['username']  
        if request.method == 'GET':
                if 'username' not in session:
                        return redirect(url_for('login'))
                else:
                         return render_template('/files/createfile.html', sesion=session,naprofile=naprofile,usuario=usuario)                  
        else: 
                name=request.form.get('name')
                file=request.files['file']
                       
                if not createfile.controllerCreateFile(name,file):
                        return render_template("/files/createfile.html",name=name,naprofile=naprofile,usuario=usuario)
                notifi = True
                return render_template("/files/createfile.html", notifi=notifi,naprofile=naprofile,usuario=usuario)

@app.route("/my-files", methods =['POST','GET'])
def listfiles():

        naprofile= nameprofile.nameprofile()
     
        usuario = session['username']   
        if request.method =="GET":
                if 'username' not in session:
                        return redirect(url_for("login"))
                else:
                        fils = files.listfiles(usuario)
                        return render_template("/files/listfiles.html",fils=fils,naprofile=naprofile,usuario=usuario)

                                
               
                

@app.route("/delete/<int:id>", )
def deletefile(id):
    if 'username' not in session:
        return redirect(url_for('login'))
    else:
        files.deletefile(id)     
        return redirect(url_for('homeusr'))

                
       
@app.route("/update-file/<int:id>",methods=['POST','GET'])
def updateFile(id):

        naprofile= nameprofile.nameprofile()
        usuario = session['username'] 
        if 'username' not in session:
                return redirect(url_for('login'))
        else:   
                if request.method == 'GET':
                        seefile= files.seefile(id)
                        status = seefile[0][7]                      
                        return render_template("/files/editfile.html",seefile=seefile,naprofile=naprofile,usuario=usuario,status=status)
                elif request.method == 'POST':
                        seefile= files.seefile(id)
                        name= request.form.get('name')
                        file=request.files['file']
                        status= request.form.get('status')
                                                
                      
                notifi = True
                if not editfile.controllerEditFile(name,file,id,status):
                        return render_template("/files/editfile.html",notifi=notifi,seefile=seefile,naprofile=naprofile,usuario=usuario,status=status)
                seefile= files.seefile(id)
                status = seefile[0][7]          
                return render_template("/files/editfile.html",notifi=notifi,seefile=seefile,usuario=usuario,naprofile=naprofile,status=status)


@app.route("/download/<id>", methods =['POST','GET'])
def Download(id):
        seefiles = files.seefile(id)     
        return send_from_directory("./static/files/",path=seefiles[0][3],as_attachment = True)



@app.route("/share/<id>", methods =['POST','GET'])
def Preview(id):

        seefiles = files.seefile(id)       
        return render_template("/files/preview.html",seefiles= seefiles,url_golbal=settings.GLOBAL_URL)


@app.route("/public", methods =['GET'])
def Publicfiles():
      
       
        if 'username' not in session:
                publicfiles = files.statusfiles()
                return render_template("/files/public.html",publicfiles=publicfiles)
        else:   
                naprofile= nameprofile.nameprofile()
                usuario = session['username']
                publicfiles = files.statusfiles()
                return render_template("/files/public.html",publicfiles=publicfiles,naprofile=naprofile,usuario=usuario)





############# ACORTADOR #############

@app.route("/home-acortador", methods=["GET","POST"])
def homeAcort():
        return render_template("/acort-url/index.html")


@app.route("/acortador", methods=["GET","POST"])
def crear():

        length_of_string = 5
        short =(''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string)))    
        if request.method=="POST": 
                isValid = True
                url=request.form["direccionURL"] 

                if url == "":
                        isValid = False
                        flash("Ingrese un link")
                        print("no hay link")
                if isValid == False:          
                        notifi = True            
                        return render_template("/acort-url/index.html",notifi=notifi)

                acortador.createUrl(url=url,short=short)
           
        return render_template("/acort-url/urlAcort.html",short=short,url=url)

@app.route("/cortar/<url_cort>",methods=["GET","POST"])
def redireccionar(url_cort):       

        url_cort= acortador.redireccionarUrl(url_cort)
        UrlDirec = url_cort[0]
        return redirect(UrlDirec)
        








              





