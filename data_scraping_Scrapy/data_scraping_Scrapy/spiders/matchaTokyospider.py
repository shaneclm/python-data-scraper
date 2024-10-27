import scrapy

class MatchaSpider(scrapy.Spider):
    # name of the spider, used for running the spider from the command line
    name = 'matchaTokyo'

    # initial URL to start scraping
    start_urls = ['https://www.the-matcha.tokyo/collections/all']

    def parse(self, response):
        for products in response.css('div.grid-view-item'):
            yield {
                'name': products.css('div.product-grid--title a::text').get(),                                          # extract product name
                'price': products.css('span.money::text').get().replace('₱', ''),                                       # extract product price
                'link': 'https://www.the-matcha.tokyo' + products.css('div.product-grid--title a').attrib['href'],      # extract product link
            }

        # locates the next page trigger 
        next_page = 'https://www.the-matcha.tokyo' + response.css('li.pagination-arrow.pagination-next a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


# Key takeaways: I found Scrapy to be much easier to debug and perform trial and error thanks to its "Shell" feature. 
# This allows me to test data extraction without impacting my code. Additionally, Scrapy provides a 
# complete package for data scraping, making the process more streamlined for its intended users.