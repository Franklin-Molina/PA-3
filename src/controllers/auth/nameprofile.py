
from flask import session
from src.models.user import UsuarioModel


def nameprofile():
    usuarioModel = UsuarioModel()                
    usuario = session['username']
    user = usuarioModel.validarUser(usuario)
    naprofile = user[0][3]

    return naprofile