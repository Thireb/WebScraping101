import os, bs4, requests



url = 'https://readvagabond.com/manga/vagabond-chapter-1-shinmen-takezo/'
os.makedirs('vagabond',exist_ok=True)
while not url=="https://readvagabond.com/manga/vagabond-chapter-328-release-date-and-spoiler/":
    res = requests.get(url)
    print(res.raise_for_status())
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    imageElement = soup.select('img')
    if imageElement == []:
        print("Nothing found.")
    else:
        imageSource = imageElement[0].get('data-src')
        print("downloading")
        res = requests.get(imageSource)
        print(res.raise_for_status())
        imageFile = open(os.path.join('vagabond',os.path.basename(imageSource)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    nextLink = soup.select('a[rel="next"]')[0]
    url = nextLink.get('href')
    
print('Done.')