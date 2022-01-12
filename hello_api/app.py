from flask import Flask , request, jsonify
from models import recipes
from http import HTTPStatus

app = Flask(__name__)

@app.route('/',methods=['GET'])
def get_all_recipes():
    """
    This method will return all the recipes
    :return: Json data with all the recipes
    """
    return jsonify(data=recipes)

@app.route('/recipes/<int:recipe_id>')
def get_recipe(recipe_id):
    recipe_found =next((recipe for recipe in recipes if recipe['id']==recipe_id),None)
    if recipe_found:
        return jsonify(recipe_found)
    return jsonify(message='recipe not found'),HTTPStatus.NOT_FOUND

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)