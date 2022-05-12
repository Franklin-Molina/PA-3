
from src.config.db import db


from smtplib import SMTP

from src.config import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class UsuarioModel():
   
    """ def crearUser(serlf,usuario,correo,claveEncritada,validate_mail,vali_url):
        cursor =db.cursor()
        cursor.execute('insert into usuario(nombre,correo,password,validate_mail,vali_url) values(%s,%s,%s,%s,%s)', (
            usuario,
            correo,
            claveEncritada,
            validate_mail,
            vali_url,

            ))       
        cursor.close()   """
    def validarUser(self,usuario,):
        cursor =db.cursor()
        
        cursor.execute('select correo,password, validate_mail, nombre from usuario where  usuario.correo = %s',(usuario,))      
        usuario = cursor.fetchall()
        cursor.close()
        return usuario

def createUser(name,email,claveEncritada,validate_mail,vali_url):
    cursor = db.cursor()
    cursor.execute("insert into usuario (nombre,correo,password,validate_mail,vali_url) values(%s,%s,%s,%s,%s)", (
        name,
        email,
        claveEncritada,
        validate_mail,
        vali_url,

    ))
    cursor.close()



def valiCorreo(valimail,content,asunto):

    
    message = MIMEMultipart()
    message['subject'] = asunto
    message['from'] = 'kiragod@gmail.com'
    message['To'] = valimail
    

    message_html = MIMEText(content, 'html')
    message.attach(message_html)

    username = settings.SMPT_USERNAME
    password = settings.SMPT_PASSWORD

    server = SMTP(settings.SMPT_HOSTNAME)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, valimail, message.as_string())

    server.quit()
    
def UsuarioValidado(validate_mail, vali_url):
    cursor = db.cursor()    
    cursor.execute('UPDATE usuario SET validate_mail = "true", vali_url = "" WHERE validate_mail="'+validate_mail+'" AND vali_url="'+vali_url+'"')
    cursor.close()
def UserVal(validate_mail,vali_url):
    cursor = db.cursor(dictionary= True)
    cursor.execute('select * from usuario where validate_mail="'+validate_mail+'" AND vali_url = "'+vali_url+'"')

    userv = cursor.fetchall()
    cursor.close()
    return userv

def SendPassword(valimail, Token_password):
    cursor = db.cursor()
    cursor.execute('UPDATE usuario SET tokenpassword = "'+Token_password+'" WHERE correo="'+valimail+'" ')
    cursor.close()

def NewPassword(newpaswd, password1):
    cursor = db.cursor()
    cursor.execute('UPDATE usuario SET password = "'+password1+'", tokenpassword="" WHERE tokenpassword="'+newpaswd+'" ')
    User = cursor.fetchone()
    
    cursor.close()
    return User


def valPassword(tokenpassword):
    cursor = db.cursor(dictionary= True)
    cursor.execute('select * from usuario where tokenpassword  = "'+tokenpassword+'"')
    valpassword = cursor.fetchall()
    cursor.close()
    return valpassword