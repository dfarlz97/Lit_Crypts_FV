from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api, Resource
import requests
from flask_cors import CORS
from random import choice
from models import Puzzle, db 

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

def fetch_quote():
    url = 'https://api.quotable.io/quotes/random?limit=50'
    data = requests.get(url).json()

    #print("Received data from API:", data)  
    
    if isinstance(data, list):
        valid_quotes = [quote['content'] for quote in data if len(quote['content']) < 100]
        #print("Valid quotes:", valid_quotes)
 
        if valid_quotes:
            return choice(valid_quotes)
    
    return None

class Puzzles(Resource):
    def get(self):
        try:
            puzzles = [p.to_dict(only=("id", "quote")) for p in Puzzle.query.all()]
            return puzzles, 200
        except:
            raise Exception({"error": "Something went wrong"})

    def post(self):
        try:
            new_puzzle = Puzzle(
                quote=fetch_quote(),  # Add a quote when creating a puzzle
            )
            db.session.add(new_puzzle)
            db.session.commit()
            return new_puzzle.to_dict(only=("id", "quote")), 201
        except:
            return {"error": "400: Validation error"}, 400
        
api.add_resource(Puzzles, "/puzzles")

if __name__ == '__main__':
    app.run(port=5555, debug=True)