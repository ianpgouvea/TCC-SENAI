from app import app

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app_tcc_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'


DEBUG = True

SECRET_KEY = 'uma-chave-segura'
