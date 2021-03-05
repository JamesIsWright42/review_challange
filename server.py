from flask import Flask, render_template
from flask import request
from scrape import get_review_list

app = Flask(__name__)

#Good Witches
#http://127.0.0.1:8000/mortgage/grander-home-loans-inc/58426567
#http://127.0.0.1:8000/personal/first-midwest-bank/52903183
#http://127.0.0.1:8000/business/ondeck/51886298
#http://127.0.0.1:8000/auto/refijet/65336845
#http://127.0.0.1:8000/student/sofi/53081129

#Bad Witches
#http://127.0.0.1:8000/student/sofye/53081129
#http://127.0.0.1:8000/student/sofi
#http://127.0.0.1:8000
@app.route('/<string:loan_type>/<string:lender>/<string:lender_id>', methods=['GET'])
def get_reviews(loan_type, lender, lender_id):
    reviews = get_review_list(loan_type, lender, lender_id)
    return reviews

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'),500