# -*- coding: utf-8 -*-
import scrapy
import re


class RatingsSpider(scrapy.Spider):
    # name = 'ratings'
    allowed_domains = ['sandiego.rubratings.com']
    start_urls = ['http://sandiego.rubratings.com/?layout=list']


    def parse(self, response):

        rub_id = response.css('a').xpath('@id').getall()
        advertising_text = response.xpath('//a/text()').getall()

        yield {
            "ID":rub_id,
            "Ad Text":advertising_text
        }

        div_item = response.xpath('//*[@class="col-md-12 list-item "]')
        for div in div_item:
            id = response.css('a').xpath('@id').extract_first()
            ad_text = div.xpath('.//*[@href]/text()').extract_first()
            l = div.xpath('.//*[@id]/following-sibling::text()').extract_first()
            location = l[2:-10]
            rub_ad_link = response.xpath('//*[@class="col-md-12 list-item "]/a/@href').extract_first()


            print('\n')
            print(id)
            print(l)
            print(location)
            print(ad_text)
            print(rub_ad_link)
            yield {
                    "id": id,
                    "ad": ad_text,
                    "location": location,
                    "advertiser_link": rub_ad_link
                    }

            #
            #
            # next_page_url = response.xpath('//*[@class="col-md-12 list-item "]/a/@href').extract_first()
            # absolute_next_page = response.urljoin(next_page_url)
            # yield {
            #    next_page_url = response.xpath('//*[@class="col-md-12 list-item "]/a/@href').extract_first()
            # }
