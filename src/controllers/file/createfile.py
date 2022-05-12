from flask import  flash,session
from src.models import user
from src.models import files
import os

from src.controllers.file import renamefile 

def controllerCreateFile(name,file):
    
    usuario = session['username']
    namefile= file.filename.lower()    
    arcot =  namefile.split(".")
    
    

    isValid= True
    if name == "":
        isValid = False
        flash("Ingrese un nombre")
    else:
        if namefile== "":
            isValid = False
            flash ("Ingrese un archivo")

    if isValid ==False:
        return False
    
    iduser = files.find_iduser(usuario)

    for id in iduser:
        idus= id
        print("usuario",idus) 
              
    typefile= arcot[-1]
   
    newname = renamefile.Renamefile(file) 
    viewfile = renamefile.previewfile(newname,typefile)

    sizefile = convert(os.stat('./src/static/files/' +newname).st_size)        
    files.createFile(user=idus,name=name,file=newname,typefile=typefile,size=sizefile,viewfile=viewfile)
 
    return True
        
    
                                   
def convert(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0