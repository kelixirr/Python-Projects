import requests, os, bs4

url = 'http://xkcd.com'

os.makedirs('xkcd', exist_ok = True)

while not url.endswith("#"):

  # Download the page
  print("Downloading page %s..." %url)
  res = requests.get(url)
  res.raise_for_status()

  soup = bs4.BeautifulSoup(res.text)
  
  # Find the URL of the comic image
  comicElem = soup.select('#comic img')
  if comicElem == []:
    print('Could not find comic image')

  else:
    comicURl = comicElem[0].get('src')

    # download the image
    print('Download image %s...' %(comicURl))
    res = requests.get(comicURl)
    res.raise_for_status()

    # save the image to file
    imageFile = open(os.path.join('okcd', os.path.basename(comicURl)), 'wb')

    for chunck in res.iter_content(100000):
      imageFile.write(chunck)

  # get the prev button's url
  prevLink = soup.select('a[rel = "prev"]')[0]
  url = 'http://xkcd.com' + prevLink.get('href')


print('Done')

