import requests
import pandas as pd
from requests_html import HTML

url = "https://www.lendingtree.com/reviews/{loan_type}/{lender}/{lender_id}"

review_list = []

review_headers = ["Review Title", "Stars", "Review", "Author", "Address", "Date"]

fetch_html_error = "failed to scrape reviews with the submitted url. URL: {url}"

parse_html_error = "failed to parse the review html from the full scraped html"

parse_text_error = "failed to parse text for field: {field}"

def get_review_list(submitted_url):
    html_text, code = fetch_review_html(submitted_url)

    if html_text == "":
        return fetch_html_error.format(url=submitted_url)

    reviews = parse_review_html(html_text)

    if reviews == parse_html_error:
        return reviews

    review_list = review_html_to_text_list(reviews)

    df = pd.DataFrame(review_list, columns=review_headers)
    review_dict = df.to_dict()
    return review_dict


def fetch_review_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        return html_text, r.status_code
    return "", r.status_code

def parse_review_html(html_text):
    r_html = HTML(html=html_text)
    review_html = r_html.find(".lenderReviews")
    if review_html == -1:
        return parse_html_error
    review_body = review_html[0]
    reviews = review_body.find(".mainReviews")
    if reviews == -1:
        return parse_html_error
    return reviews

def review_html_to_text_list(reviews):
    for review in reviews:
        review_fields = []

        review_fields.append(parse_review_title(review))

        review_fields.append(parse_star_rating(review))

        review_fields.append(parse_review_text(review))

        name, address = parse_name_and_address(review)

        review_fields.append(name)

        review_fields.append(address)

        review_fields.append(parse_review_date(review))

        review_list.append(review_fields)

    return review_list

def parse_review_title(review):
    review_title = review.find(".reviewTitle")
    if review_title == -1:
        return parse_text_error.format(field="Review Title")
    return review_title[0].text

def parse_star_rating(review):
    star_reviews = review.find(".starReviews")
    if star_reviews == -1:
        return parse_text_error.format(field="Stars")
    stars_and_rec = star_reviews[0].text
    star_rec = stars_and_rec.split("stars")
    return star_rec[0]

def parse_review_text(review):
    review_text = review.find(".reviewText")
    if review_text == -1:
        return parse_text_error.format(field="Review")
    return review_text[0].text

def parse_name_and_address(review):
    consumer_name = review.find(".consumerName")
    if consumer_name == -1:
        return parse_text_error.format(field="Reviewer"), parse_text_error.format(field="Address")
    name_and_address = consumer_name[0].text
    name_add = name_and_address.split(" from ")
    return name_add[0], name_add[1]

def parse_review_date(review):
    review_date = review.find(".consumerReviewDate")
    if review_date == -1:
        return parse_text_error.format(field="Date")
    return review_date[0].text