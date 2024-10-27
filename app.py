from flask import render_template
from flask import Flask, request
import getVerse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    verse_text = "En el principio creó Dios los cielos y la tierra."
    book, chapter, verse = "genesis", 1, 1


    if request.method == 'POST':
        book = request.form['book']
        chapter = int(request.form['chapter'])
        verse = int(request.form['verse'])

        # Call the function to get the Bible verse
        verse_text = getVerse.verse_text(book, chapter, verse)

        # List of books, chapters, and verses for the dropdowns

    books = ["genesis", "exodo", "leviticos", "numeros", "deuteronomios", "josue", "jueces", "rut",
             "1samuel", "2samuel", "1reyes", "2reyes", "1cronicas", "2cronicas", "esdras", "nehemias",
             "ester", "job", "salmos", "proverbios"]

    chapters = list(range(1, 51))  # Modify based on the book's chapter range
    verses = list(range(1, 51))  # Modify based on the chapter's verse rang

    return render_template('index.html',
                           books=books,
                           chapters=chapters,
                           verses=verses,
                           verse_text=verse_text,
                           selected_verse=[book, chapter, verse])

if __name__ == '__main__':
    app.run(debug=True)