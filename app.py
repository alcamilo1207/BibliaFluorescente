from flask import render_template
from flask import Flask, request
import getVerse

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    verse_text = "En el principio creó Dios los cielos y la tierra."
    book, chapter, verse = "genesis", '1', '1'
    chapters = list(range(1, 51))  # Modify based on the book's chapter range
    verses = list(range(1, 32))  # Modify based on the chapter's verse rang

    if request.method == 'POST':
        book = request.form['book']
        chapter = request.form['chapter']
        verse = request.form['verse']

        # List of books, chapters, and verses for the dropdowns
        chapters = getVerse.get_chapterList(book)  # Modify based on the book's chapter range
        verses = getVerse.get_verseList(book,chapter)  # Modify based on the chapter's verse rang

        if int(chapter) > len(chapters):
            chapter = '1'

        if int(verse) > len(verses):
            verse = '1'

        # Call the function to get the Bible verse
        verse_text = getVerse.verse_text(book, chapter, verse)



    book_names = ["Génesis", "Éxodo", "Levítico", "Números","Deuteronomio","Josué","Jueces","Rut","1 Samuel",
                  "2 Samuel","1 Reyes","2 Reyes","1 Crónicas","2 Crónicas","Esdrás","Nehemías","Ester",
                  "Job","Salmos","Proverbios","Eclesiastés","Cantares","Isaías","Jeremías","Lamentaciones",
                  "Ezequiel","Daniel","Oseas","Joel","Amós","Abdías","Jonás","Miqueas","Nahum", "Habacuc","Sofonías",
                  "Hageo", "Zacarías", "Malaquías"]



    return render_template('index.html',
                           books=book_names,
                           chapters=chapters,
                           verses=verses,
                           verse_text=verse_text,
                           selected_verse=[book, chapter, verse])

if __name__ == '__main__':
    app.run(debug=True)
