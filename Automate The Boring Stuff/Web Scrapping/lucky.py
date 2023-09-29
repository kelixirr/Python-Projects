import requests, sys, webbrowser, bs4 

# CL arguments and requests the search page
print('Googling...')

# The user will specify the search terms using command line arguments. These arguments will be stored as strings in a list in sys.argv

res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))

res.raise_for_status()

# retrieve the top search result links
soup = bs4.BeautifulSoup(res.text, features="html.parser")

# Open a browser tab for each result
linkElems = soup.select('.r a')
numOpen =  min(5, len(linkElems))
for i in range(numOpen):
  webbrowser.open('http://google.com' + linkElems[i].get('href'))