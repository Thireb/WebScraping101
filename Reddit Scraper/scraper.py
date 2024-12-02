from kcu import kjson
from reddit_scraper.reddit_scraper import RedditScraper


id_ = "bitcoin"
post = RedditScraper.get_posts(id_)
print(len(post))
print(post)
