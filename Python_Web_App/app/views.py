from flask import Flask, Response, request, redirect, url_for
from app import app
url = '''
<html>
  <head>
    <meta charset="utf-8">
    <title>File Maker</title>
    <style type="text/css">
      button {
        display: block;
        margin: 0 auto;
        margin-top: 10px;
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        font-size: 20px;
      }
    </style>
  </head>
  <body style="background-color:#a6d8a8">
    <form action="/html/" method="post">
      <button type="submit">HTML Document</button>
    </form>
    <form action="/css/" method="post">
      <button type="submit">CSS Document</button>
    </form>
    <form action="/js/" method="post">
      <button>JS Document</button>
    </form>
    <form action="/python/" method="post">
      <button>Python Document</button>
    </form>
    <form action="/jquery/" method="post">
      <button>JQuery Library</button>
    </form>
  </body>
  <script>
    if(window.location == "http://localhost:5000/html/") {
        window.history.back();
    } else if(window.location == "http://localhost:5000/css/") {
        window.history.back();
    } else if(window.location == "http://localhost:5000/js/") {
        window.history.back();
    } else if(window.location == "http://localhost:5000/python/") {
        window.history.back();
    } else if(window.location == "http://localhost:5000/jquery/") {
        window.history.back();
    }
  </script>
</html>
'''

# ======== MAIN WEBPAGE ======== #
@app.route('/')
@app.route('/index')
def index():
    return url
# ======== MAIN WEBPAGE ======== #


# ======== LOAD HTML DOCUMENT ======== # 
@app.route("/html/", methods=["POST"])
def createHTMLDoc():
     newDoc = open("C:/Users/Owner/Desktop/index.html", "w")
     return url
# ======== LOAD HTML DOCUMENT ======== #


# ======== LOAD CSS DOCUMENT ======== #
@app.route("/css/", methods=["POST"])
def createCSSDoc():
     newDoc = open("C:/Users/Owner/Desktop/index.css", "w")
     return url
# ======== LOAD CSS DOCUMENT ======== #


# ======== LOAD JS DOCUMENT ======== #
@app.route("/js/", methods=["POST"])
def createJSDoc():
     newDoc = open("C:/Users/Owner/Desktop/index.js", "w")
     return url
# ======== LOAD JS DOCUMENT ======== #


# ======== LOAD Python DOCUMENT ======== #
@app.route("/python/", methods=["POST"])
def createPythonDoc():
     newDoc = open("C:/Users/Owner/Desktop/index.py", "w")
     return url
# ======== LOAD Python DOCUMENT ======== #


# ======== LOAD JQuery LIBRARY ======== #
@app.route("/jquery/", methods=["POST"])
def createJQueryDoc():
     newDoc = open("C:/Users/Owner/Desktop/jquery.js", "w")
     return url
# ======== LOAD JQuery LIBRARY ======== #


