from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import urllib.request

startingpage = "https://www.youtube.com/watch?v=pcK_IidPfMA";
buffer = [startingpage]

def FixURL(pageurl, linkurl):
	# makes stub urls full urls	
	newurl = urljoin(pageurl, linkurl)
	afterslash = urlparse(newurl).path.rsplit('/', 1)[-1] # just get the filename
	if urlparse(newurl).query != '':
		afterslash += "?" + urlparse(newurl).query
	newurl = urljoin(newurl, './' + afterslash) # completely normalise
	return newurl

def GetLinks(url):
	links = []
	# get page html
	try:
		response = urllib.request.urlopen(url)
	except:
		return links
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	atags = soup.findAll("a")
	for atag in atags:
		if atag.has_attr('href'):
			href = FixURL(url, atag['href'])
			links.append(href)
	return links

def Crawl(url):
	print(len(buffer)) # number in buffer
	links = GetLinks(url)
	for link in links:
		buffer.append(link)
	buffer.remove(url)

# main
#GetLinks(startingpage)
while 1 == 1:
	for url in buffer:
		Crawl(url)