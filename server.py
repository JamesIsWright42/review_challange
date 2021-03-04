from flask import Flask
from flask import request
from scrape import get_review_page

app = Flask(__name__)

#http://127.0.0.1:8000/mortgage/grander-home-loans-inc/58426567
@app.route('/<string:loan_type>/<string:lender>/<string:lender_id>', methods=['GET'])
def get_reviews(loan_type, lender, lender_id):
    reviews = get_review_page(loan_type, lender, lender_id)
    return reviews