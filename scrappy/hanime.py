import scrapy


class ExtractUrls(scrapy.Spider):

	# This name must be unique always
	name = "extract"

	# Function which will be invoked
	def start_requests(self):

		# enter the URL here
		urls = ['https://hanime.tv/browse/images', ]

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)
