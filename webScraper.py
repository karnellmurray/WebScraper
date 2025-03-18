import scrapy

class CultBeautySpider(scrapy.Spider):
    name = "cultbeauty"
    start_urls = ["https://www.cultbeauty.co.uk/p/elemis-superfood-midnight-facial-50ml/13207745/"]

    def parse(self, response):
        for review in response.css("div#review-wrapper div.py-8.flex.flex-col.gap-4.border-b"):
            yield {
                'title': review.css('h4::text').get(),  # Extract title of the review 
                
                # Extract the rating from the number of filled SVG stars
                'rating': len(review.css('div.rating svg path[fill]')),
                
                'content': review.css('p::text').getall(),  # Extract the content of the review
                'date': review.css('time::attr(datetime)').get(),  # Extract the review date
                'author': review.css('p.font-bold time::text').get(),  # Extract the author's name
            }
