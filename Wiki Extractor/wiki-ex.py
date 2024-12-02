import csv
import wikipedia as wiki
import csv

search_articles = ['light','astronomy','fossils','android','plants','animals','ocean','oxygen']
# with open('wikis.txt','w') as textWriteFile:
#     for keyword in search_articles:
#         for query in wiki.search(wiki.suggest(keyword), results=25):
#             textWriteFile.write(wiki.summary(query))
#print(len(wiki.search('Python Programming', results=100)))
# for keyword in search_articles:
#     print(keyword)
#     print(len(wiki.search(keyword, results=100)))
#     print()
#     # for query in wiki.search(keyword, results=2):
    #     p = wiki.page(query)
    #     print(keyword,p.title)
#----------------------csv-write-----------------------------
# with open('wikionek.csv','w') as csvWriterFile:
#     writer = csv.writer(csvWriterFile)
#     writer.writerow(['Title','Body'])
#     for keyword in search_articles:
#         for query in wiki.search(keyword,results=2):
#             p = wiki.page(query)
#             writer.writerow([p.title,wiki.summary(query)])
# for keyword in search_articles:
#     #suggested = wiki.suggest(keyword)
#     result = wiki.search(keyword,results=1)
result = 'gradient_bound_objective'
word = wiki.suggest(result)
for query in wiki.search(word):
    p = wiki.page(query)
    print(p.title)