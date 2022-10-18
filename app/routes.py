from app import app
from flask import render_template

@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/fav')
def fav():
    games = ['Elden Ring','Dark Souls','Bloodborne','Destiny','God of War']
    return render_template('fav.html', names=games)