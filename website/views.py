from flask import Blueprint, render_template, request, redirect, url_for, session, abort, make_response, jsonify
from flask_session import Session
import random, time
from datetime import datetime

import os

from werkzeug.utils import secure_filename


views = Blueprint("views", __name__)


POSTS = []

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def covert_to_bytes(path):
  with open(path, 'rb') as fp:
    return fp.read()

@views.route("/")
def home():
  return render_template("index.html")

@views.route("/feed", methods=["GET","POST"])
def feed():
  path_ = ""
  image_ = False
  if request.method == 'POST':

    if "image" in request.files:
      image = request.files["image"]
      image_ = True
      if allowed_file(image.filename):
        filename = secure_filename(image.filename)

        path_ = f"static/user_image/imagetosave_{len(POSTS) + 1}.png"
        path = f"website/static/user_image/imagetosave_{len(POSTS) + 1}.png" 
        image.save(path)
        image_ = covert_to_bytes(path)
        # os.remove(path)
        
          
      
      
    else:
      print("No image found!")


    


    content = request.form.get("content")
    current_time = datetime.now()
    human_readable_time = current_time.strftime("%Y-%m-%d %I:%M:%S %p")
    
    if image_ and path_ != "":
      POSTS.append([session["username"], content, human_readable_time, path_])
    else:
      POSTS.append([session["username"], content, human_readable_time])
    
    return redirect(url_for("views.feed"))
  if session["username"] is not None: 
    return render_template("feed.html", posts=POSTS[::-1])
    
  else:
    return redirect(url_for("auth.logout"))

@views.route("/rooms")
def rooms():
  if session["username"] is not None: 
    return render_template("rooms.html")
    
  else:
    return redirect(url_for("auth.logout"))


@views.route("/about")
def about():
  if session["username"] is not None: 
    return render_template("about.html")
    
  else:
    return redirect(url_for("auth.logout"))

