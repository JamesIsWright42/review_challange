import pytest

from scrape import fetch_review_html, parse_review_html
from test_structures import parse_review_html_resp
from test_html import test_html_resp




def test_fetch_review_html():
    test_url = "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183"
    test_html = fetch_review_html(test_url)

    assert len(test_html) == 270653

def test_parse_review_html():
    test_reviews = parse_review_html(test_html_resp)
    assert len(test_reviews) == 10
