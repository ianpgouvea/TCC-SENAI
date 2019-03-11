from wtforms import Form, StringField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('', [validators.Length(min=1, max=50, message='Nome deve conter de 1 a 50 digitos')])
    cpf = StringField('', [validators.Length(min=4, max=25, message='CPF deve conter de 4 a 50 digitos')])
    email = StringField('', [validators.Length(min=6, max=50, message='Email deve conter de 6 a 50 digitos')])
    password = StringField('', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Senha inválida')
    ])
    confirm = PasswordField('')
