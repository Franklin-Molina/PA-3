from datetime import datetime
import os

def Renamefile(newfile):

    time =  datetime.now()

    namefile = newfile.filename
    namefile = namefile.split(".")
    newname = str(namefile[1])+'-'+str(time.date())+'-'+str(time.hour)+'-'+str(time.minute)+'-'+str(time.second)+'-'+str(time.microsecond)+'.'+str(namefile[-1])

    newfile.save('./src/static/files/' + newfile.filename)
    os.rename('./src/static/files/' + newfile.filename,'./src/static/files/' + newname )
    
    return newname


def previewfile(file,typefile):
    
    routefile = "/static/img/typesfiles/no-disponible.png"

    if  typefile in ['png','jpg','gif']:
        routefile = "/static/files/" + file    
    if typefile == 'pdf':
        routefile = "/static/img/typesfiles/pdf.png"
    if typefile == 'xlsx':
        routefile = "/static/img/typesfiles/excel.png"
    if typefile == 'pptx':
        routefile = "/static/img/typesfiles/powerpoint.png"
    if typefile == 'docx':
        routefile = "/static/img/typesfiles/word.png"
    if typefile == 'mp3':
        routefile = "/static/img/typesfiles/mp3.png"
    if typefile in ['mp4','mkv','avi']:
        routefile = "/static/img/typesfiles/mp4.png"
    if typefile == 'exe':
        routefile = "/static/img/typesfiles/exe.png"         

    return routefile
