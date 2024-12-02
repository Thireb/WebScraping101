import requests 

res = requests.get(
    'https://19-14.b.cdn13.com/022/433/434/144p.h264.mp4', stream=True)
res.raise_for_status()
imageFile = open('video_2.mp4', 'wb')
for chunk in res.iter_content(1000000):
    imageFile.write(chunk)
imageFile.close
