from posixpath import basename
import requests, os, bs4

for x in range(1,98):
    url = 'https://w16.read-chainsawman.com/manga/chainsaw-man-chapter-' + str(x) +'/'
    folderName = 'chainsaw-man-chapter-'+ str(x)
    os.makedirs(folderName, exist_ok=True)
#download the page
    print("Downloading the page %s" %url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    mangaImage = soup.select('p > img')
    if mangaImage == []:
        print('Could not find image.')
        
    else:
#find url of image
        numOpen = max(1, len(mangaImage))
        for i in range(numOpen):
            mangaURL = mangaImage[i].get('src')
            print("Downloading Image %s" %(mangaURL))
            res = requests.get(mangaURL)
            res.raise_for_status()
            fileName = 'Image number: ' + str(i)
    #Save file to ./chainsaw
            pathImage = os.path.join(folderName, fileName)
        #print(pathImage)
            imageFile = open(pathImage,'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close
            
            
    
print("Done.")