from flask import Flask
from flask import request
from scrape import get_review_list

app = Flask(__name__)

#http://127.0.0.1:8000/mortgage/grander-home-loans-inc/58426567
#http://127.0.0.1:8000/personal/first-midwest-bank/52903183
#http://127.0.0.1:8000/business/ondeck/51886298
#http://127.0.0.1:8000/auto/refijet/65336845
#http://127.0.0.1:8000/student/sofi/53081129
@app.route('/<string:loan_type>/<string:lender>/<string:lender_id>', methods=['GET'])
def get_reviews(loan_type, lender, lender_id):
    reviews = get_review_list(loan_type, lender, lender_id)
    return reviews