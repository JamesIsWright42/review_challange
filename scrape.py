import requests
import pandas as pd
from requests_html import HTML


lender_name = "grander-home-loans-inc"

lender_product_type = "mortgage"

lender_url_id = "58426567"

url = "https://www.lendingtree.com/reviews/{loan_type}/{lender}/{lender_id}"

review_list = []

review_headers = ["Lender", "Loan Type", "Review Title", "Stars", "Recommendation", "Review", "Reviewer", "Address", "Date"]


def get_review_page(lender, lender_id, url):
    html_text = fetch_review_html(url)
    if html_text == "":
        return "failed to scrape reviews with the submitted fields"
    review_html_to_text_list(html_text)


def fetch_review_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text
    return ""

def review_html_to_text_list(html_text):
    
    r_html = HTML(html=html_text)
    review_html = r_html.find(".lenderReviews")
    parsed_reviews = review_html[0]
    reviews = parsed_reviews.find(".mainReviews")

    for review in reviews:
        review_fields = []

        review_fields.append(lender_name)

        review_fields.append(lender_product_type)

        review_title = review.find(".reviewTitle")

        review_fields.append(review_title[0].text)

        star_reviews = review.find(".starReviews")
        stars_and_rec = star_reviews[0].text

        star_rec = stars_and_rec.split("stars")

        review_fields.append(star_rec[0])
        review_fields.append(star_rec[1])

        review_text = review.find(".reviewText")

        review_fields.append(review_text[0].text)

        consumer_name = review.find(".consumerName")
        name_and_address = consumer_name[0].text
        name_add = name_and_address.split("from ")

        review_fields.append(name_add[0])
        review_fields.append(name_add[1])

        review_date = review.find(".consumerReviewDate")
        review_fields.append(review_date[0].text)

        review_list.append(review_fields)

    # df = pd.DataFrame(review_list, columns=review_headers)
    # df.to_csv('reviews.csv', index=False)

get_reviews(lender_name, lender_url_id)