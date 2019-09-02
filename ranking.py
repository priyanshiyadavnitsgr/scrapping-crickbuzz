from scrapy import Spider, Request

class ranking(Spider):
    name='ranking'
    start_urls=['https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting']

    def parse(self, response):
        ranks=response.css('#page-wrapper > div > div> div > div > div > div ')

        for rank in ranks:
            yield{
                'rank':rank.css('div:nth-child(1)::text').extract_first(),
                'name':rank.css('div:nth-child(2) div:nth-child(2) a::text').extract_first(),
                'bio':rank.css('div:nth-child(2) div:nth-child(2) a::attr("href")').extract_first(),
                'rating':rank.css('div:nth-child(3)::text').extract_first()
            }

 #document.querySelector("#page-wrapper > div.cb-col.cb-col-100.cb-bg-white.ng-scope > div.cb-col.cb-col-67.cb-scrd-lft-col > div > div > div:nth-child(1) > div:nth-child(2) > div.cb-col.cb-col-16.cb-rank-tbl.cb-font-16")