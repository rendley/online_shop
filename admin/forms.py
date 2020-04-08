from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError
from .models import User


# flask tutorial Form Validation with WTForms - The Forms
class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    # def validate_username(self, name): 
    #     user_count = User.query.filter_by(name=name.data).count() # запрос имени в базе
    #     if user_count > 0:
    #         raise ValidationError("Пользователь с таким именем уже существует")

    # def validate_email(self, email): 
    #     email_count = User.query.filter_by(email=email.data).count()
    #     if email_count > 0:
    #         raise ValidationError("Пользователь с таким почтовым адресом уже существует")


class LoginForm(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired()])

