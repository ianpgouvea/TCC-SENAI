from flask import Flask, render_template, flash, redirect, url_for, request, session, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

from app.models.form import RegisterForm
from app import app


db = MySQL(app)

@app.route('/teste')
def teste():
    return render_template('')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servico-online')
def servicoOnline():
    return render_template('servico-online.html')

@app.route('/admin/despachante')
def login_admin():
    return render_template('/include/admin/home-admin.html')

@app.route('/admin/despachante/pedidos')
def pedidos():
    return render_template('/include/admin/pedidos.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #Pegando os campos do formulario
        cpf = request.form.get('cpf')
        password_candidate = request.form.get('password')

        #Criando o cursor
        cur = mysql.connection.cursor()

        #Pegando um usuario pelo CPF
        result = cur.execute("SELECT * FROM users WHERE cpf = %s", [cpf])

        if result > 0:
            #Get started hash
            data = cur.fetchone()
            password = data['password']

            #Comparando as senhas pelo hash
            if sha256_crypt.verify(password_candidate, password):
                app.logger.info('PASSWORD MATCHED')
            else:
                error = 'Login inválido'
                return render_template('login.html', error=error)
        else:
            error = 'CPF não encontrado'
            return render_template('login.html', error=error)

    return render_template('login.html')

@app.route('/admin/despachanteOn')
def adminDespachante():
    return render_template('/include/admin/admin-despachante.html')

@app.route('/informativo')
def informativo():
    return render_template('informativo.html')

@app.route('/servico')
def servico():
    return render_template('servico.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            name = form.name.data
            email = form.email.data
            cpf = form.cpf.data
            password = sha256_crypt.encrypt(str(form.password.data))

            # Criando o Cursor
            cur = db.connection.cursor()

            cur.execute("INSERT INTO users(name, email, cpf, password) VALUES(%s, %s,  %s, %s )", (name, email, cpf, password))


            #Commit DB
            db.connection.commit()

            #Fechando conexao
            cur.close()

            flash('Cadastro efetuado com sucesso','success')

            return redirect(url_for('login'))


        return render_template('register.html', form=form)
