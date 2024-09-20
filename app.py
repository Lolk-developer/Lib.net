from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = "=v4QI!oi;4vKXqY2VLbwGh&QTpzT;1P1-&'gRZErEvF9--$N]1%?/)wLdWt\.Yh&$)ONu.?+q>TiI"
admin = Admin(app, name='Lib.net-админка')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.Text, nullable=False)
    book_name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    links = db.Column(db.String(100), nullable=False)


@app.route('/')
@app.route('/main')
def main():
    return render_template("index.html")


@app.route('/classic_foreign')
def classic_foreign():
    classic_foreign_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='classic_foreign').all()
    return render_template("classic_foreign.html", classic_foreign_books=classic_foreign_books)


@app.route('/classic_ru')
def classic_ru():
    classic_ru_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='classic_ru').all()
    return render_template("classic_ru.html", classic_ru_books=classic_ru_books)


@app.route('/comedy')
def comedy():
    comedy_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='comedy').all()
    return render_template("comedy.html", comedy_books=comedy_books)


@app.route('/documental')
def documental():
    documental_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='documental').all()
    return render_template("documental.html", documental_books=documental_books)


@app.route('/dramma')
def dramma():
    dramma_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='dramma').all()
    return render_template("dramma.html", dramma_books=dramma_books)


@app.route('/fantasy')
def fantasy():
    fantasy_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='fantasy').all()
    return render_template("fantasy.html", fantasy_books=fantasy_books)


@app.route('/horror')
def horror():
    horror_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='horror').all()
    return render_template("horror.html", horror_books=horror_books)


@app.route('/student')
def student():
    student_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='student').all()
    return render_template("student.html", student_books=student_books)


@app.route('/tragedy')
def tragedy():
    tragedy_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='tragedy').all()
    return render_template("tragedy.html", tragedy_books=tragedy_books)


@app.route('/triller')
def triller():
    triller_books = Books.query.order_by(Books.genre, Books.id.desc()).filter_by(genre='triller').all()
    return render_template("triller.html", triller_books=triller_books)


@app.route('/easter_egg')
def easter_egg():
    return render_template("easter_egg.html")


@app.route('/easter_egg/Tyler_Derden')
def Derden():
    return render_template("derden.html")


@app.route('/<category>/<int:id>')
def Book(id, category):
    list_category = ("classic_ru", "classic_foreign", "comedy", "documental", "dramma", "fantasy", "horror", "student", "tragedy", "triller")
    if category in list_category:
        book = Books.query.get(id)
        return render_template("book.html", book=book)


@app.route('/<category>/upload', methods=['POST', 'GET'])
def upload(category):
    list_category = ("classic_ru", "classic_foreign", "comedy", "documental", "dramma", "fantasy", "horror", "student", "tragedy", "triller")
    if request.method == "POST":
        author_name = request.form['author_name']
        book_name = request.form['book_name']
        description = request.form['description']
        links = request.form['links']
        if category in list_category:
            genre_choose = category
            new_book = Books(author_name=author_name, book_name=book_name, description=description, genre=genre_choose, links=links)
            db.session.add(new_book)
            db.session.commit()
            return redirect(f'/{category}')
    return render_template("upload.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    query = request.form["query"]
    search_book = Books.query.order_by(Books.book_name, Books.id.desc()).filter_by(book_name=query).all()
    return render_template("results.html", search_book=search_book, query=query)


admin.add_view(ModelView(Books, db.session))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")