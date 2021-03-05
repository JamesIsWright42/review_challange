from flask import Flask, render_template, request
from scrape import get_review_list

app = Flask(__name__)

#http://127.0.0.1:8000/form
@app.route('/form', methods=['GET', 'POST'])
def get_reviews_from_url():
    if request.method == 'POST':
        url = request.form.get('url')
        reviews = get_review_list(url)
        return reviews

    return '''
           <form method="POST">
               <div><label>URL: <input type="text" name="url"></label></div>
               <input type="submit" value="Submit">
           </form>'''

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500