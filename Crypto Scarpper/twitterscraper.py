from Scweet.scweet import scrape
data = scrape(words=['bitcoin'], since="2021-10-01", until="2021-10-02", from_account=None, interval=1,
              headless=False, display_type="Top", save_images=False, lang="en",
              resume=False, filter_replies=False, proximity=False, geocode="38.3452,-0.481006,200km")
text = data['Text']
print(text)