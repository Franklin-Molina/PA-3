from dotenv import load_dotenv
import os

#Carga el archivo .env a las variables de entorno
load_dotenv()

MYSQL_HOSTNAME= os.environ.get('MYSQL_HOSTNAME')
MYSQL_USERNAME= os.environ.get('MYSQL_USERNAME')
MYSQL_PASSWORD= os.environ.get('MYSQL_PASSWORD')
MYSQL_DATABASE= os.environ.get('MYSQL_DATABASE')
MYSQL_PORT= os.environ.get('MYSQL_PORT')

SMPT_HOSTNAME= os.environ.get('SMPT_HOSTNAME')
SMPT_USERNAME= os.environ.get('SMPT_USERNAME')
SMPT_PASSWORD= os.environ.get('SMPT_PASSWORD')


GLOBAL_URL= os.environ.get('GLOBAL_URL')