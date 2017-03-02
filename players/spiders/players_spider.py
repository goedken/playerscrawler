import scrapy
import json
import requests
from players.items import Player

class PlayersSpider(scrapy.Spider):
    name = "players"

    with open('player_links.json') as data_file:
        data = json.load(data_file)

    start_urls = []
    for link in data:
        print start_urls.append(link['player_url'])


    # start_urls = [
    #     'http://www.espn.com/nba/teams/roster?team=BOS',
    #     'http://www.espn.com/nba/teams/roster?team=BKN',
    #     'http://www.espn.com/nba/teams/roster?team=NY',
    #     'http://www.espn.com/nba/teams/roster?team=PHI',
    #     'http://www.espn.com/nba/teams/roster?team=TOR',
    #     'http://www.espn.com/nba/teams/roster?team=CHI',
    #     'http://www.espn.com/nba/teams/roster?team=CLE',
    #     'http://www.espn.com/nba/teams/roster?team=DET',
    #     'http://www.espn.com/nba/teams/roster?team=IND',
    #     'http://www.espn.com/nba/teams/roster?team=MIL',
    #     'http://www.espn.com/nba/teams/roster?team=ATL',
    #     'http://www.espn.com/nba/teams/roster?team=CHA',
    #     'http://www.espn.com/nba/teams/roster?team=MIA',
    #     'http://www.espn.com/nba/teams/roster?team=ORL',
    #     'http://www.espn.com/nba/teams/roster?team=WSH',
    #     'http://www.espn.com/nba/teams/roster?team=GS',
    #     'http://www.espn.com/nba/teams/roster?team=LAC',
    #     'http://www.espn.com/nba/teams/roster?team=LAL',
    #     'http://www.espn.com/nba/teams/roster?team=PHX',
    #     'http://www.espn.com/nba/teams/roster?team=SAC',
    #     'http://www.espn.com/nba/teams/roster?team=DAL',
    #     'http://www.espn.com/nba/teams/roster?team=HOU',
    #     'http://www.espn.com/nba/teams/roster?team=MEM',
    #     'http://www.espn.com/nba/teams/roster?team=NO',
    #     'http://www.espn.com/nba/teams/roster?team=SA',
    #     'http://www.espn.com/nba/teams/roster?team=DEN',
    #     'http://www.espn.com/nba/teams/roster?team=MIN',
    #     'http://www.espn.com/nba/teams/roster?team=OKC',
    #     'http://www.espn.com/nba/teams/roster?team=POR',
    #     'http://www.espn.com/nba/teams/roster?team=UTAH'
    # ]

    def parse(self, response):
        for player in response.css('body'):
            image_url = player.css('div.main-headshot img::attr(src)').extract_first()
            yield {
                'image_url': image_url
            }
            # team_name = team.css('a.sub-brand-title b::text').extract_first()
            #
            # links = team.css('td.sortcell a[href*="player/_/id/"]::attr(href)').extract()
            #
            # player_item = Player()
            # player_item['team_name'] = team_name
            # player_item['image_urls'] = []
            #
            # for link in links:
            #
            #     yield {
            #         'player_url': link
            #     }
                # player_item['image_urls'].append(scrapy.Request(link, callback=self.parse_player))
                # yield scrapy.Request(link, callback=self.parse_player)

    def parse_player(self, response):
        # player_item = response.meta['item']

        image_url = response.css('div.main-headshot img::attr(src)').extract_first()
        # player_item['image_urls'].append(image_url)

        return image_url

            # index = int(response.url.split('/')[7])
            # name = player.css('div.mod-content h1::text').extract_first()
            # team = player.css('div.player-bio ul.general-info li.last a::text').extract_first()
            # posnum = player.css('div.player-bio ul.general-info li.first::text').extract_first()
            # number = posnum[1:3]
            # position = posnum.split()[1]
            # heightweight = player.css('div.player-bio ul.general-info li::text').extract()[1]
            # height = heightweight.split(',')[0]
            # weight = heightweight.split(',')[1][1:]
            # age = player.css('div.player-bio ul.player-metadata li::text').extract()[0]
            # age = age.split(':')[1][1:3]
            # bio_size = len(player.css('div.player-bio ul.player-metadata li::text').extract())
            # college = player.css('div.player-bio ul.player-metadata li::text').extract()[bio_size - 2]
            # experience = player.css('div.player-bio ul.player-metadata li::text').extract()[bio_size - 1]
            # ppg = player.css('div.player-stats table.header-stats tr td::text').extract()[0]
            # stat1key = player.css('div.player-stats table.header-stats th::text').extract()[1]
            # stat2key = player.css('div.player-stats table.header-stats th::text').extract()[2]
            # stat1value = player.css('div.player-stats table.header-stats tr td::text').extract()[1]
            # stat2value = player.css('div.player-stats table.header-stats tr td::text').extract()[2]
            # per = player.css('div.player-stats table.header-stats tr td::text').extract()[3]

            # index = 1
            # name = player.css('div.players div[id="meta"] h1[itemprop="name"]::text').extract_first()
            # team = player.css('div.players div[id="meta"] a[href*="teams"]::text').extract_first()
            # number = player.css('div.uni_holder text::text').extract_first()
            # position = 'SF'
            # height = player.css('span[itemprop="height"]::text').extract_first()
            # weight = player.css('span[itemprop="weight"]::text').extract_first()
            # age = '22'
            # college = 'None'
            # experience = '3 years'
            # ppg = player.css('div.stats_pullout div.p1 p::text').extract()[3]
            # rpg = player.css('div.stats_pullout div.p1 p::text').extract()[5]
            # apg = player.css('div.stats_pullout div.p1 p::text').extract()[7]
            # per = player.css('table[id="advanced"] td[data-stat="per"]::text').extract_first()
            # ortg = player.css('table[id="per_poss"] td[data-stat="off_rtg"]::text').extract_first()
            #
            # playeritem = Player()
            # playeritem['id'] = index
            # playeritem['name'] = name
            # playeritem['team'] = team
            # playeritem['number'] = number
            # playeritem['position'] = position
            # playeritem['height'] = height
            # playeritem['weight'] = weight
            # playeritem['age'] = age
            # playeritem['college'] = college
            # playeritem['experience'] = experience
            # playeritem['ppg'] = ppg
            # playeritem['stat1key'] = 'rpg'
            # playeritem['stat2key'] = 'apg'
            # playeritem['stat1value'] = rpg
            # playeritem['stat2value'] = apg
            # playeritem['per'] = per
            # playeritem['ortg'] = ortg

            # image_url = player.css('div.main-headshot img::attr(src)').extract_first()
            # print image_url
            # with open('images/pic' + str(index) + '.jpg', 'wb') as handle:
            #     response = requests.get(image_url, stream=True)
            #
            #     if not response.ok:
            #         print response
            #
            #     for block in response.iter_content(1024):
            #         if not block:
            #             break
            #
            #         handle.write(block)

            # yield playeritem

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