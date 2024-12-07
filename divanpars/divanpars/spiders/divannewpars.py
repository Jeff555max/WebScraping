import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "depanneurs"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        divans = response.css('div._Ud0k')
        # Настраиваем работу с каждым отдельным диваном в списке
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }
