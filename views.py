from flask import Blueprint, render_template, request, redirect, url_for, session
from flask_session import Session
import random, time
from datetime import datetime

views = Blueprint("views", __name__)


POSTS = []



@views.route("/")
def home():
  return render_template("index.html")

@views.route("/feed", methods=["GET","POST"])
def feed():

  if request.method == 'POST':
    content = request.form.get("content")
    current_time = datetime.now()
    human_readable_time = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    POSTS.append([session["username"], content, human_readable_time])
    
    return redirect(url_for("views.feed"))
  if session["username"] is not None: 
    return render_template("feed.html", posts=POSTS[::-1])
    
  else:
    return redirect(url_for("auth.logout"))


@views.route("/about")
def about():
  if session["username"] is not None: 
    return render_template("about.html")
    
  else:
    return redirect(url_for("auth.logout"))

