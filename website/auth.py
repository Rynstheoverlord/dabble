from flask import Blueprint, request, redirect, render_template, url_for, session
import time

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
  if "username" not in session:
    session["username"] = None
  if request.method == 'POST':
    username = request.form.get("username")
    session['username'] = username
    session["last_post"] = 0
    return redirect(url_for("views.feed"))
  return render_template("login.html")


@auth.route("/logout")
def logout():
  session["username"] = None
  return redirect(url_for("auth.login"))
