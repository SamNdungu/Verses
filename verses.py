from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:samwayneke@localhost/verses'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://pgkorivefmktjz:e6b26e8065dc8a251b82ff76f09864cd49a8069efb03324175a651157c64aeba@ec2-34-197-25-109.compute-1.amazonaws.com:5432/defonuihvobmn1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class FavouriteVerses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String(30))
    verse = db.Column(db.String(2000))




@app.route('/')
def index():
    result = FavouriteVerses.query.all()
    return render_template('index.html', result=result)


@app.route('/verses')
def verses():
    return render_template('verses.html')  


@app.route('/process', methods = ['POST'])
def process():
    book = request.form['book']
    verse = request.form['verse']
    versedata = FavouriteVerses(book=book, verse=verse)
    db.session.add(versedata)
    db.session.commit()

    return redirect(url_for('index'))   


