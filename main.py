# -*- coding: utf-8 -*-
import urllib2

def find_href(url):
    links_arr = []
    link = urllib2.urlopen(url).read()
    links_available = 'true'
    while links_available == 'true':
        corpus = link.find("href")
        if corpus >= 0:
            link_len = len(link)
            link = link[corpus:link_len]
            corpus = link.find('"')
            link_len = len(link)
            link = link[corpus + 1:link_len]
            corpus = link.find('"')
            needle = link[0:corpus]

            if needle.startswith("http" or "www"):
                links_arr.append(needle)
        else:
            links_available = 'false'
    return links_arr

def find_src(url):
    links_arr = []
    link = urllib2.urlopen(url).read()
    links_available = 'true'
    while links_available == 'true':
        corpus = link.find("src")
        if corpus >= 0:
            link_len = len(link)
            link = link[corpus:link_len]
            corpus = link.find('"')
            link_len = len(link)
            link = link[corpus + 1:link_len]
            corpus = link.find('"')
            needle = link[0:corpus]

            if needle.startswith("/"):
                needle = url + needle
                links_arr.append(needle)
        else:
            links_available = 'false'
    return links_arr
            

if __name__ == '__main__':
    url = "http://gbvmexico.com"
    links = find_href(url) + find_src(url)

    for i in links:
        print i


