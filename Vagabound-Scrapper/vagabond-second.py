import bs4, requests,os
x=1
stopingURL = "https://readvagabond.com/manga/vagabond-chapter-328-release-date-and-spoiler/" 
url = 'https://readvagabond.com/manga/vagabond-chapter-1-shinmen-takezo/' #url of the website, with autoincrementing chapters 

while url != stopingURL: #to loop through all of the chapters
    print("IN while loop.")
    folderName = 'vagabond-chapter-' + str(x) #create a folders, with autoincreasing digits as chapters
    os.makedirs(folderName, exist_ok=True) #create folders
    print("folder-"+folderName)
    
    res = requests.get(url) #request/get the url
    print(res.raise_for_status()) #check url's status
    soup = bs4.BeautifulSoup(res.text, 'html.parser') #give the requested url to bs4 parser
    mangaImage = soup.select('img') #select all image tags in a list
    if mangaImage == []:
        print('Could not find image.')
    else:
        numOpen = max(1, len(mangaImage)) #get max length of image tags
        for i in range(numOpen): #loop through all of the image tags and get their source
            mangaURL = mangaImage[i].get('data-src') #get source of each image's tag
            print('Downloading Image %s'%(mangaURL))  
            res = requests.get(mangaURL) #get URL of one image's source
            print(res.raise_for_status())
            fileName = 'img_'+str(i)+'.png' #create file name of downloaded image to write it as.
            pathImage = os.path.join(folderName, fileName) #file name with folder and image name combined
            imageFile = open(pathImage,'wb') #open file name in write binary form to write image
            for chunk in res.iter_content(100000): #start writing image in bytes of 100,000
                imageFile.write(chunk) #writing image to image file name
            imageFile.close #close image file 
    nextLink = soup.select('a[rel="next"]')[0]
    url = nextLink.get('href')
    x += 1
print('Done.')
