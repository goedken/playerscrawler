import scrapy
import requests
from players.items import Player

class PlayersSpider(scrapy.Spider):
    name = "players"

    start_urls = [
        'http://www.espn.com/nba/player/_/id/3032977/giannis-antetokounmpo',
        'http://www.espn.com/nba/player/_/id/3418/michael-beasley',
        'http://www.espn.com/nba/player/_/id/2566769/malcolm-brogdon',
        'http://www.espn.com/nba/player/_/id/2489716/matthew-dellavedova',
        'http://www.espn.com/nba/player/_/id/3211/spencer-hawes',
        'http://www.espn.com/nba/player/_/id/6592/john-henson',
        'http://www.espn.com/nba/player/_/id/3436/roy-hibbert',
        'http://www.espn.com/nba/player/_/id/4017843/thon-maker',
        'http://www.espn.com/nba/player/_/id/6609/khris-middleton',
        'http://www.espn.com/nba/player/_/id/4260/greg-monroe',
        'http://www.espn.com/nba/player/_/id/3056600/jabari-parker',
        'http://www.espn.com/nba/player/_/id/2528353/tony-snell',
        'http://www.espn.com/nba/player/_/id/4385/mirza-teletovic',
        'http://www.espn.com/nba/player/_/id/841/jason-terry',
        'http://www.espn.com/nba/player/_/id/3137733/rashad-vaughn'
    ]

    def parse(self, response):
        for player in response.css('body'):
            index = int(response.url.split('/')[7])
            name = player.css('div.mod-content h1::text').extract_first()
            team = player.css('div.player-bio ul.general-info li.last a::text').extract_first()
            posnum = player.css('div.player-bio ul.general-info li.first::text').extract_first()
            number = posnum[1:3]
            position = posnum.split()[1]
            heightweight = player.css('div.player-bio ul.general-info li::text').extract()[1]
            height = heightweight.split(',')[0]
            weight = heightweight.split(',')[1][1:]
            age = player.css('div.player-bio ul.player-metadata li::text').extract()[0]
            age = age.split(':')[1][1:3]
            bio_size = len(player.css('div.player-bio ul.player-metadata li::text').extract())
            college = player.css('div.player-bio ul.player-metadata li::text').extract()[bio_size - 2]
            experience = player.css('div.player-bio ul.player-metadata li::text').extract()[bio_size - 1]
            ppg = player.css('div.player-stats table.header-stats tr td::text').extract()[0]
            apg = player.css('div.player-stats table.header-stats tr td::text').extract()[1]
            rpg = player.css('div.player-stats table.header-stats tr td::text').extract()[2]
            per = player.css('div.player-stats table.header-stats tr td::text').extract()[3]

            playeritem = Player()
            playeritem['id'] = index
            playeritem['name'] = name
            playeritem['team'] = team
            playeritem['number'] = number
            playeritem['position'] = position
            playeritem['height'] = height
            playeritem['weight'] = weight
            playeritem['age'] = age
            playeritem['college'] = college
            playeritem['experience'] = experience
            playeritem['ppg'] = ppg
            playeritem['apg'] = apg
            playeritem['rpg'] = rpg
            playeritem['per'] = per
            playeritem['image_name'] = 'pic' + str(index) + '.jpg'

            image_url = player.css('div.main-headshot img::attr(src)').extract_first()
            print image_url
            with open('images/pic' + str(index) + '.jpg', 'wb') as handle:
                response = requests.get(image_url, stream=True)

                if not response.ok:
                    print response

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

            yield playeritem

# id = scrapy.Field()
# name = scrapy.Field()
# team = scrapy.Field()
# number = scrapy.Field()
# position = scrapy.Field()
# height = scrapy.Field()
# weight = scrapy.Field()
# age = scrapy.Field()
# college = scrapy.Field()
# experience = scrapy.Field()
# ppg = scrapy.Field()
# apg = scrapy.Field()
# rpg = scrapy.Field()
# per = scrapy.Field()