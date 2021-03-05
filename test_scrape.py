import pytest

from scrape import fetch_review_html, parse_review_html, parse_html_error
from test_structures import parse_review_html_resp
from test_html import test_html_resp




def test_fetch_review_html():
    test_url = "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183"
    test_html, status_code = fetch_review_html(test_url)

    assert status_code == 200
    assert test_html != ""

def test_parse_review_html():
    test_reviews = parse_review_html(test_html_resp)
    assert len(test_reviews) == 10
    assert test_reviews != parse_html_error
