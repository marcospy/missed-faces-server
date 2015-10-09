from flask import Blueprint, redirect
import flask

from flask.ext.login import login_user, login_required, logout_user

from flask.globals import request
from flask.helpers import url_for

from flask.templating import render_template

from application.apps.auth.forms import SignInForm, LoginForm
from application.apps.auth.models import User

auth_mod = Blueprint('auth', __name__, url_prefix='')


@auth_mod.route("/cadastro", methods=['GET'])
def signin_form():
    form = SignInForm()
    return render_template("signin.html", form=form)


@auth_mod.route("/cadastro", methods=['POST'])
def signin():
    form = SignInForm()

    if form.validate_on_submit():
        user = User()

        user.email = form.data['email']
        user.password = form.data['password']

        user.save()

        login_user(user)
        return redirect("/")
    else:
        print form.errors

    return render_template("signin.html", form=form)


@auth_mod.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.objects.get(email=form.data['email'])
            login_user(user)
            return redirect(request.args.get('next') or url_for("index"))

    return render_template("login.html", form=form)


@auth_mod.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect("/login")
