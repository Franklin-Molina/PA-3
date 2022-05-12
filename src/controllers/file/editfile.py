from flask import  flash,session
from src.models import files
import os

from src.controllers.file import renamefile 

def controllerEditFile(name,file,id_arch,status):
    
    usuario = session['username']
    namefile= file.filename.lower()    
    arcot =  namefile.split(".")
    
    if status is None:
        status = 'private'
    else:
        status = 'public'        
          
    isValid= True
    if name == "":
        isValid = False
        flash("Ingrese un nombre")
        return False
    
    if isValid ==False:
        return False
    
    iduser = files.find_iduser(usuario)

    for id in iduser:
        idus= id
        #print("usuario",idus) 
        

        
    if file.filename == "":
        #print("No hay archivo")
        files.upnamefile(name=name,id=id_arch,status=status)
    else:
        typefile= arcot[-1]
   
        newname = renamefile.Renamefile(file) 
        viewfile = renamefile.previewfile(newname,typefile)

        sizefile = convert(os.stat('./src/static/files/' +newname).st_size)
      
        files.updatefile(id=id_arch,name=name,file=newname,typefile=typefile,size=sizefile,viewfile=viewfile,status=status)
 
    return True
        
    
                                   
def convert(num):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0