from flask import  flash
from src.models.user import UsuarioModel
from src.models import user
from werkzeug.security import generate_password_hash, check_password_hash

import random ,string
import re
from src.models.user import UsuarioModel




def controllerNewPassword(password1,newpaswd):
                
    enciptar = generate_password_hash(password1)

    isValid= True
    lenpass =  len(password1)
    minuscula = False
    mayuscula= False
    numeros = False
    special = False
                

    if password1 == "":
        flash("Contraseña Obligatoria")  
        isValid=False  
    else:
        if lenpass < 8 :                       
            flash("La contraseña debe tener minimo 8 caracteres")                       
            isValid=False                
        else:
            for caracter in password1:
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
                        if re.search('[@_!#$%^&*()<>?/\|}{~:]',password1):                        
                            special= True
                                                                                
                        if special == False:
                            isValid=False
                            flash("Ingrese un caracter a la contraseña")
    if isValid == False:
        return False
    
    user.NewPassword(newpaswd=newpaswd,password1=enciptar)

    return True
                
                