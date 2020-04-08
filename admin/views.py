from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db, bcrypt
from .forms import RegistrationForm, LoginForm
from .models import User





@app.route('/admin/', methods=['GET', 'POST'])
def admin():
    return render_template("admin/index.html", title="Admin")



# flask tutorial Form Validation with WTForms - In the View
@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, email=form.email.data, password=hash_password)
        db.session.add(user)       
        db.session.commit()
        flash(f'Привет {form.name.data}. Вы успешно зарегистрировались!', "success")
        return redirect(url_for("login"))
    else:           
        flash("Проверить  ", "danger")
        return render_template('admin/register.html',title='Register user', form=form)
    # add except email and name




    
        
# or check name and password
@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session["email"] = form.email.data
            flash(f"Привет {form.email.data}, вы успешно зашли на сайт!", "success")
            return redirect(request.args.get("next") or url_for("admin"))
        else:           
            flash("Неверный адрес электронный почты или пароль", "danger")

    return render_template("admin/login.html", form=form, title="Login page")


