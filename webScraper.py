# Import Scrapy
import scrapy

# Scrapy class - This is the web scraping function, it passes the url and gets the information from the HTML (website) elements
class CultBeautySpider(scrapy.Spider):

    name = "cultbeauty"

    # CHANGE THIS URL FOR ANY CULT BEAUTY PRODUCTS YOU WANT TO GET REVIEWS FOR
    start_urls = ["https://www.cultbeauty.co.uk/p/elemis-superfood-midnight-facial-50ml/13207745/"]

    def parse(self, response):
        for review in response.css("div#review-wrapper div.py-8.flex.flex-col.gap-4.border-b"):
            yield {
                # REVIEW HEADERS
                'title': review.css('h4::text').get(),  # Extract Title
                'rating': len(review.css('div.rating svg path[fill]')), # Extract Rating             
                'content': review.css('p::text').getall(),  # Extract Content (Actual review)
                'date': review.css('time::attr(datetime)').get(),  # Extract Date (review was made)
                'author': review.css('p.font-bold time::text').get(),  # Extract the author's name (Person who wrote review)
            }

# READ THIS TO RUN PROGRAM
# When you have changed the URL and you have a product you want to get the reviews for, copy and paste this command in the terminal and press enter

# scrapy runspider webScraper.py -o reviews.json  

# CHECK REVIEWS.JSON <<<<< FILE FOR THE RESULTS 


