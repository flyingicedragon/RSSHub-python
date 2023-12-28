#!/usr/bin/env python3

from rsshub.utils import fetch
from parsel import Selector

domain = 'https://www.fjtv.net'


def parse(post: Selector) -> dict:
    item = {}
    item['title'] = post.xpath('a/@title').get()
    _ = post.xpath('a/@href').get()
    assert _ is not None
    if not _.startswith('http'):
        item['link'] = f'https:{_}'
    else:
        item['link'] = _
    item['pubData'] = post.xpath('span/text()').get()
    _ = fetch(item['link'])
    assert _ is not None
    item['description'] = _.xpath('//input[@id=\'m3u8\']/@value').get()
    item['author'] = '福建网络广播电视台'
    return item


def ctx(id: str) -> dict:
    id = id.replace('_', '/')
    url = f'{domain}/{id}'
    tree = fetch(url)
    assert tree is not None
    title = tree.xpath('//a[@class=\'itb-title\']/text()').get()
    desc = tree.xpath('//div[@class=\'jieshao_desc\']/text()').get()
    posts = tree.xpath('//ul[@class=\'clearfix page-split\']/li')
    return {
        'title': f'福建网络广播电视台 - {title}',
        'link': url,
        'description': desc,
        'author': 'flyingicedragon',
        'items': list(map(parse, posts)),
    }
