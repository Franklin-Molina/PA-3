from src.config.db import db

def createFile(user,name,file,typefile,size,viewfile):
    cursor = db.cursor()
    cursor.execute ("insert into files (id_user,name,file,typefile,size,viewfile,status) values (%s,%s,%s,%s,%s,%s,'private')",(
        user,
        name,
        file,
        typefile,
        size,
        viewfile,
    ))
    cursor.close()

def find_iduser(usuario):
    cursor = db.cursor()
    cursor.execute("select id from usuario where correo = %s",(usuario,))
    iduser = cursor.fetchone()
    return iduser
        
def listfiles(usuario):
    cursor = db.cursor()
    #cursor.execute("select * from files,usuario where files.id_user = usuario.id and usuario.correo= %s",(usuario,))
    cursor.execute("select * from files,usuario where files.id_user = usuario.id and usuario.correo= %s",(usuario,))
    listfiles = cursor.fetchall()

    cursor.close()
    return listfiles

def deletefile(id):
    cursor = db.cursor()
    cursor.execute("delete from files where files.id=%s",(id,))
    cursor.close()
  

def seefile(id):
    cursor = db.cursor()
    cursor.execute("select  * from files where files.id=%s",(id,))
    file = cursor.fetchall()        
    cursor.close()
    return file

def updatefile(name,id,file,typefile,size,viewfile,status):
    cursor = db.cursor()
    cursor.execute("update files set name = %s, file = %s, typefile = %s, size = %s, viewfile = %s , status= %s  where files.id=%s",(
        name,  
        file,
        typefile,
        size,
        viewfile,
        status,
        id,
        
    ))
    cursor.close()

def upnamefile(name,status,id):
    print(id)
    cursor = db.cursor()
    cursor.execute("update files set name = %s , status= %s  where files.id=%s",(
        name,  
        status,
        id,
    ))
    cursor.close()


def statusfiles():    
    cursor = db.cursor()
    cursor.execute("select  * from files where status = 'public'")
    publicfiles = cursor.fetchall()        
    cursor.close()
    return publicfiles
