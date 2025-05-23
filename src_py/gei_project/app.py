from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask("D&K")
CORS(app)

client = MongoClient("mongodb://localhost:27017/")  
db = client["cookit"]  
recipes_collection = db["recipes"]  

@app.route('/')
def index():
    return 'Flask-приложение работает!БД MongoDB подключена!'

@app.route('/recipes', methods=['POST'])
def get_recipes():
    data = request.json
    ingredients = data.get('ingredients', [])

    if not ingredients:
        return jsonify([])

    recipes = recipes_collection.find({
        "ingredients": {"$all": ingredients}
    })
    result = [
        {"name": recipe["name"], "ingredients": recipe["ingredients"]}
        for recipe in recipes
    ]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
