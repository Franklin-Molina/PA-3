from flask import  flash
from src.models.user import UsuarioModel
from src.models import user
import random ,string
from src.config import settings



def controllerRecoverPassword(email):
    usuarioModel = UsuarioModel()
    isValid= True

    if  usuarioModel.validarUser(usuario=email):
        Token_password = ""
        for i in range(15):
            Token_password += random.choice(string.ascii_letters)                                
                        
        asunto= "Recuperar password"
        content= '<p>Hola , para recuperar su contraseña ingrese  :</p><a href="'+settings.GLOBAL_URL+'/recuper-password/'+Token_password+'"> Aquí</a>'


        user.SendPassword(valimail=email,Token_password=Token_password) 
        user.valiCorreo(valimail=email,content=content,asunto=asunto)             
                                                              
    else:
        isValid=False
        flash("El correo no existe")
                   
    if isValid == False: 
        return False
    return True