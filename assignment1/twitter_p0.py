import urllib
import json
import sys

def main():
  if len(sys.argv) > 2:
    print 'usage: ./wordcount.py [query]'
    sys.exit(1)

  query = "microsoft"

  if len(sys.argv) == 2:
    query = sys.argv[1]
  
  tweets_only = []
  for j in range(1,2):
    x = open('tweets.txt','a')
    response = urllib.urlopen("http://search.twitter.com/search.json?q=" + query + "&page=" + str(j))
    download = json.load(response)

    tweets = download['results']
    i = 0
    while i < len(tweets):
      print "Tweet #" + str(i) + ": " + tweets[i]['text'].encode('utf-8')
      tweets_only.append(tweets[i]['text'])
      i += 1
    
    x.write(download)
    x.close()
  
  

  
if __name__ == '__main__':
  main()
