import pytest
import pytest_vcr
from urllib import request



from scrape import fetch_review_html, parse_review_html




@pytest.mark.vcr()
def test_iana():
    response = request.urlopen('http://www.iana.org/domains/reserved').read()
    assert b'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183' in response


def test_fetch_review_html():
    test_url = "https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183"
    test_html, status_code = fetch_review_html(test_url)

    assert status_code == 200
    assert test_html != ""

def test_parse_review_html():
    test_reviews = parse_review_html(test_html_resp)
    assert len(test_reviews) == 10
    assert test_reviews != parse_html_error
