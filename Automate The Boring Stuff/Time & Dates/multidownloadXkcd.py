import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok= True)

def downloadXkcd(startComic, endComic):
  for urlNumber in range(startComic, endComic):

    # download the page
    print('Download page  http://xkcd.com/%s...' % (urlNumber))
    res = requests.get('http://xkcd.com/%s' % (urlNumber))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the url of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
      print('Could not find comic image.')
    
    else:
      comicURl = comicElem[0].get('src')
      # download the image
      print('Downloading image %s...' % (comicUrl))
      res = requests.get(comicURl)
      res.raise_for_status()

      #save the image to file
      imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), "wb")
      for chunk in res.iter_content(100000):
        imageFile.write(chunk)
      imageFile.close()


# Create and start the Thread objects
downloadThreads = []

for i in range(0, 1400, 100):
  downloadThread = threading.Thread(target=downloadXkcd, args = (i, i + 99))
  downloadThreads.append(downloadThread)
  downloadThread.start()

# wait for all threads to end
for downloadThread in downloadThreads:
  downloadThread.join()
  print('Done.')
