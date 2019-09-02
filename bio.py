from scrapy import Spider, Request

class bio(Spider):
    name='bio'
    start_urls=['https://www.cricbuzz.com/cricket-stats/icc-rankings/men/batting']

    def parse(self, response):
        for href in response.css('#page-wrapper > div > div> div > div > div > div div:nth-child(2) div:nth-child(2) a::attr(href)'):
            yield response.follow(href, self.parse_bio)

    def parse_bio(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('#playerProfile > div > div > h1::text'),
            'country':extract_with_css('#playerProfile > div > div > h3::text'),
            'category':extract_with_css('#playerProfile > div > div >div > div:nth-child(15)::text'),
            'test_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(16)::text'),
            'odi_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(17)::text'),
            't20_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(18)::text'),
            'category':extract_with_css('#playerProfile > div > div >div > div:nth-child(19)::text'),
            'test_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(20)::text'),
            'odi_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(21)::text'),
            't20_ranking':extract_with_css('#playerProfile > div > div >div > div:nth-child(22)::text'),
            
        }

        #//*[@id="playerProfile"]/div[2]/div[1]/div/div[19]
        # document.querySelector("#playerProfile > div.cb-col.cb-col-100.cb-bg-grey > div.cb-col.cb-col-33.text-black > div > div:nth-child(19)")
        # document.querySelector("#playerProfile > div.cb-col.cb-col-100.cb-bg-white > div.cb-col.cb-col-80.cb-player-name-wrap > h1")