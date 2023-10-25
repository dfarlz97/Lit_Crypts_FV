from models import db, Puzzle
from app import app, fetch_quote

def create_puzzles():

    puzzles = []

    for i in range(100):
        quote = fetch_quote() 
        p = Puzzle(quote=quote) 
        db.session.add(p)
        puzzles.append(p)
        db.session.commit()
    
    return puzzles


if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        puzzles = create_puzzles()