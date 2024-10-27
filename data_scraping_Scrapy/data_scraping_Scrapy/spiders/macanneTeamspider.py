import scrapy

class MacanneTeamSpider(scrapy.Spider):
    name = 'macanneTeam'
    start_urls = ['https://macanne.co.uk/our-team/']

    def parse(self, response):
        # select the specific div using the correct CSS selector
        target_div = response.css('div.post-content')

        # check if the target div exists
        if target_div:        
            index = 0
            column_classes = [f'div.fusion-builder-column-{i}' for i in range(17, 25)]
            selector = ', '.join(column_classes)

            # iterate over the team columns inside the target div
            for team in target_div.css(selector):
                name_index = index * 2 + 2
                position_index = name_index + 1
                image_index = 9 + index

                # for debugging
                # print(name_index)
                # print(position_index)

                yield {
                    'name': team.css(f'div.fusion-text-{name_index} h5 strong::text').get(default='No Name'),
                    'position': team.css(f'div.fusion-text-{position_index} p em::text').get(default='No Position'),
                    'image': team.css(f'span.imageframe-{image_index} img').attrib.get('data-orig-src'), 
                }

                index = index + 1

            index = 0
            column_classes = [f'div.fusion-builder-column-{i}' for i in range(28, 38)]
            selector = ', '.join(column_classes)
            for team in target_div.css(selector):
                name_index = index * 2 + 20
                position_index = name_index + 1
                image_index = 17 + index

                # for debugging
                # print(name_index)
                # print(position_index)

                yield {
                    'name': team.css(f'div.fusion-text-{name_index} h5 ::text').get(default='No Name'),
                    'position': team.css(f'div.fusion-text-{position_index} p em::text').get(default='No Position'),
                    'image': team.css(f'span.imageframe-{image_index} img').attrib.get('data-orig-src'), 
                }

                index = index + 1

        else:
            self.logger.warning('Target div not found!')


# [IGNORE] for personal documentation purposes
# logic thought process for complicated HTML classes:
#  - target a specific div
#  - find pattern within the target data
# 
# REMEMBER: when calling the response function, it returns a list of selector objects that match the specified selector from the HTML response.
#           if there are multiple elements matching the CSS selector, it will return all of them in a SelectorList, which can be iterated over.
#
