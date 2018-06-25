import urllib2
from HTMLParser import HTMLParser
from urlparse import urlparse

class LinkParser(HTMLParser):
    links = set()
    
    def handle_starttag(self, tag, attributes):
        if tag == 'a':
            attributes_dict = dict(attributes)
            if attributes_dict.get('href'):
                self.links.add(attributes_dict['href'])

        if tag == "img":
            attributes_dict = dict(attributes)
            if attributes_dict.get('src'):
                self.links.add(attributes_dict['src'])

def get_links(html, domain):
    links = set()
    parser = LinkParser()
    parser.feed(html)

    for links in parser.links:
        url_parser = urlparse(links)
        if links.startswith('/'):
            links.add(url_parser.path)
        else:
            if url_parser.netloc == domain:
                links.add(url_parser.path)
    return links


    

