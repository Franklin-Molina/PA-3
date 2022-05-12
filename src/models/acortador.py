from src.config.db import db

def createUrl(short,url):
    cursor = db.cursor()
    cursor.execute('insert into acortador(link_corto, link_original) values (%s,%s)',(short,url))
    cursor.close()
    
def redireccionarUrl(url_cort):
    cursor = db.cursor()
    cursor.execute("SELECT link_original from acortador where link_corto = %(link_corto)s",{'link_corto':url_cort})
    result=cursor.fetchone()
    return result