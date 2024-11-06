from flask import Flask, render_template, request
from recommender import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_id = int(request.form['user_id'])
    recommended_movie_titles = main(user_id)
    
    return render_template('index.html', user_id=user_id, recommendations=recommended_movie_titles)

if __name__ == '__main__':
    app.run(debug=True)
