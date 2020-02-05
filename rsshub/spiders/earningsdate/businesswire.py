from rsshub.utils import fetch, filter_content

domain = 'https://www.businesswire.com'

def parse(post):
    item = {}
    item['title'] = post.css('span[itemprop=headline]::text').extract_first().strip()
    item['description'] = item['title']
    item['link'] = f"{domain}{post.css('a.bwTitleLink::attr(href)').extract_first()}"
    item['pubDate'] = post.css('time::text').extract_first().strip()
    return item

def ctx(category=''):
    tree = fetch(f"{domain}/portal/site/home/template.PAGE/news/")
    posts = tree.css('.bwNewsList li')
    items = list(map(parse, posts)) 
    items = filter_content(items)
    return {
        'title': 'Earnings Date - Prnewswire',
        'link': f'{domain}/portal/site/home/template.PAGE/news/',
        'description': 'Earnings Date - Prnewswire',
        'author': 'hillerliao',
        'items': items
    }