
from flask import flash, request, session
from src.models.user import UsuarioModel
from werkzeug.security import  check_password_hash


def controllerLogin(usuario,password):
        usuarioModel = UsuarioModel()
        user = usuarioModel.validarUser(usuario)
        result = validardateuser(user,password)
        isValid = True
        
        if usuario == "":
                isValid =False
                flash("Ingrese un correo")
        else:
                if password == "":
                        isValid= False
                        flash("Ingrese una contraseña")
                else:
                        if not usuarioModel.validarUser(usuario=usuario) :
                                isValid = False
                                flash("La cuenta no existe")
                                
                        if user is not None and result==True : 

                                print("Usuario:",user[0][3])            
                                session['username'] = usuario
                              
                                
                        else:
                                isValid = False
                                        
        if isValid == False:
                        return False
        return True    

def validardateuser(usuario,password):
        
        isValid = True
        for user in usuario:
                print (usuario)
                if check_password_hash(user[1],password) == True:
                        if user[2]== 'true':
                                name= user[3]
                                print("Welcome:"+name)
                                print("datos bien")
                                
                                return True
                        else:
                                isValid = False
                                flash("Cuenta no verificada")
                                return False
                else:
                        isValid = False
                        flash("Email / Password incorrect")
        if isValid == False:
                return False        