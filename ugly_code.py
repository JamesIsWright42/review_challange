import datetime
import requests
import pandas as pd
from requests_html import HTML

now = datetime.datetime.now()
year = now.year

def url_to_txt(url, filename="review.html", save=False):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        if save:
            with open(f"review-{now}-{year}.html", 'w') as f:
                f.write(html_text)
        return html_text
    return ""

url = "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183"

html_text = url_to_txt(url)

r_html = HTML(html=html_text)

review_class = ".lenderReviews"
r_reviews = r_html.find(review_class)


parsed_reviews = r_reviews[0]
reviews = parsed_reviews.find(".mainReviews")
review_list = []
review_headers = ["Company", "Review Title", "Stars", "Recomendation", "Review", "Reviewer", "Address", "Date"]
company_name = "Planet Express"

for review in reviews:
    review_fields = []

    review_fields.append(company_name)

    #review_title has the title of the review
    review_title = review.find(".reviewTitle")
    review_fields.append(review_title[0].text)

    #star_score currently contains both the star_score and the recommended boolian
    star_score = review.find(".starReviews")
    star = star_score[0].text
    star_rec = star.split("stars")

    review_fields.append(star_rec[0])
    review_fields.append(star_rec[1])

    #review_text has the body of the review
    review_text = review.find(".reviewText")
    review_fields.append(review_text[0].text)

    #review_name has the name and address of the customer
    reviewer_name = review.find(".consumerName")
    revieweraddress = reviewer_name[0].text
    name_add = revieweraddress.split("from ")

    review_fields.append(name_add[0])
    review_fields.append(name_add[1])

    #review_date has the date of the review
    review_date = review.find(".consumerReviewDate")
    review_fields.append(review_date[0].text)

    review_list.append(review_fields)

df = pd.DataFrame(review_list, columns=review_headers)
df.to_csv('reviews.csv', index=False)