from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://movie_list:movie_list@localhost:8889/movie_list'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'Y2M3C1A4'

class Movies(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    releaseYear = db.Column(db.String(120))
    genre = db.Column(db.String(120))
    director = db.Column(db.String(120))
    orgin = db.Column(db.String(120))
    wikiPage = db.Column(db.String(120))
    plot = db.Column(db.String(120))

    def __init__(self, title, releaseYear, genre, director, orgin, wikiPage, plot):
        self.title = title
        self.releaseYear = releaseYear
        self.genre = genre
        self.director = director
        self.orgin = orgin
        self.wikiPage = wikiPage
        self.plot = plot

@app.route('/')
def index():
    movies = Movies.query.all()
    
    return render_template('index.html', title="Movie List!", movies=movies)

@app.route('/list')
def list():
    movies = Movies.query.all()
    return render_template('list.html')

@approute('/remove')
def remove():

@approute('/edit')
def edit():

@approute('/search')
def search():

@app.route('/addMovie', methods=['GET', 'POST'])
def addMovie():
    if request.method == 'GET':
        return render_template('addMovie.html', title="Add a Movie")

    if request.method == 'POST':
        title = request.form['movies_title']
        releaseYear = request.form['movies_releaseYear']
        genre = request.form['movies_genre']
        orgin = request.form['movies_orgin']
        director = request.form['movies_director']
        wikiPage = request.form['movies_wikiPage']
        plot = request.form['movies_plot']
        
        if title == "":
            flash("YOU NEED A TITLE!!!","error")
            return redirect('/addMovie')

        if releaseYear == "":
            flash("YOU NEED A RELEASE YEAR!!!","error")
            return redirect('/addMovie')

        if genre == "":
            flash("YOU NEED A GENRE!!!","error")
            return redirect('/addMovie')

        if director == "":
            flash("YOU NEED A DIRECTOR!!!","error")
            return redirect('/addMovie')

        if orgin == "":
            flash("YOU NEED AN ORGIN!!!","error")
            return redirect('/addMovie')
        
        if wikiPage == "":
            flash("YOU NEED A WIKIPAGE!!!","error")
            return redirect('/addMovie')

        if plot == "":
            flash("YOU NEED A PLOT!!!","error")
            return redirect('/addMovie')
            
        else: 
            addMovie = Movies(title, releaseYear, genre, director, orgin, wikiPage, plot)
            db.session.add(addMovie)
            db.session.commit()
            return render_template('movieInformation.html')


if __name__ == '__main__':
    app.run()