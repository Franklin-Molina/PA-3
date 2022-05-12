
from flask import  flash
from src.config.settings import GLOBAL_URL
from src.models.user import UsuarioModel
from src.models import user


import random ,string
from werkzeug.security import generate_password_hash, check_password_hash
import re
from src.config import settings

def controllerCreate(name,email,password):
        usuarioModel = UsuarioModel()                 
        isValid=True
        lenpass =  len(password)
        minuscula = False
        mayuscula= False
        numeros = False
        special = False
        valimail = False

                
                  
        if name == "":
                flash("Nombre Obligatorio")
                isValid=False        
        else:
                if email == "":
                        flash("Correo Obligatorio")   
                        isValid=False
                else:   
                        
                                                             
                        if re.search("(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])",email):
                                valimail= True
                        if valimail == False:
                                isValid=False  
                                flash("Correo no valido") 
                        else:   
                                if  usuarioModel.validarUser(usuario=email):
                                        isValid = False
                                        flash("El correo ya existe")                                                   
                                elif password == "":
                                        flash("Contraseña Obligatoria")  
                                        isValid=False  
                                else:
                                        if lenpass < 8 :                       
                                                flash("La contraseña debe tener minimo 8 caracteres")                       
                                                isValid=False                
                                        else:
                                                for caracter in password:
                                                        if caracter.islower() == True:  
                                                                                minuscula = True
                                                        if caracter.isupper()== True:
                                                                                mayuscula= True
                                                        if caracter.isdigit()==True:
                                                                                numeros= True                 
                                                if mayuscula == False:
                                                        isValid=False
                                                        flash("Ingrese una mayuscula a la contraseña")
                                                else:
                                                        if minuscula == False:
                                                                isValid=False
                                                                flash("Ingrese una minuscula a la contraseña")
                                                        else:              
                                                                if numeros == False:
                                                                        isValid=False
                                                                        flash("Ingrese un número a la contraseña")
                        
                                                                else:
                                                                        if re.search('[@_!#$%^&*()<>?/\|}{~:]',password):                        
                                                                                special= True
                                                                                
                                                                        if special == False:
                                                                                isValid=False
                                                                                flash("Ingrese un caracter a la contraseña")
        if isValid==False:
                    return False


        #Validacion con correo!!
        claveEncritada= generate_password_hash(password)
        validate_mail = ""  
        for i in range(4):
                validate_mail += random.choice(string.ascii_letters)
        vali_url = ""
        for i in range(15):
                 vali_url += random.choice(string.ascii_letters)
        user.createUser(name=name,email=email,claveEncritada=claveEncritada,validate_mail=validate_mail,vali_url=vali_url) 
        asunto= "Correo de validacion"
        content= '<p>Hola '+name+', para validar su cuentra ingrese :</p><a href="'+settings.GLOBAL_URL+'/val-acount/'+vali_url+'?token='+validate_mail+'"> Aquí</a>'
        user.valiCorreo(valimail=email,content=content,asunto=asunto)
    

        
        return True





""" def controllerRegMail(name,email,password):
    claveEncritada= generate_password_hash(password)
    validate_mail = ""                
    for i in range(4):
        validate_mail += random.choice(string.ascii_letters)

    vali_url = ""
    for i in range(15):
        vali_url += random.choice(string.ascii_letters)

    user.createUser(name=name,email=email,claveEncritada=claveEncritada,validate_mail=validate_mail,vali_url=vali_url) 

    

               
    asunto= "Correo de validacion"
    content= '<p>Hola '+name+', para validar su cuentra ingrese :</p><a href="http://127.0.0.1:5000/val-acount/'+vali_url+'?token='+validate_mail+'"> Aquí</a>'
    user.valiCorreo(valimail=email,content=content,asunto=asunto) """
    

    
