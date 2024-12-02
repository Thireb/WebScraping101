from rotten_tomatoes_scraper.rt_scraper import MovieScraper, CelebrityScraper

celebrity_scraper = CelebrityScraper(celebrity_name='Hugh Jackman')
celebrity_scraper.extract_metadata(section='highest')
movie_titles = celebrity_scraper.metadata['movie_titles']
print(movie_titles)



movie_scraper = MovieScraper(movie_url='https://www.rottentomatoes.com/m/the_batman')
movie_scraper.extract_metadata()

print(movie_scraper.metadata)
