import sys
import io
import json

def assign_sentiment(tfile, sdict):
   tweet_score = []
   for tweet in tfile:
      words = tweet.split()
      score = 0
      for word in words:
         if word in sdict:
            word_score = sdict[word]
         else:
            word_score = 0
         score = score + int(word_score)
      tweet_score.append(score)
   return tweet_score

def transform_AFINN(sfile):
   afinn = {}
   for line in sfile:
      tmp = line.split('\t')
      afinn[tmp[0]] = tmp[1]
   return afinn

def lines(fp):
   print str(len(fp.readlines()))

def main():
   if len(sys.argv) < 3:
      print "Usage: tweet_sentiment.py sentiment_file tweets"
      sys.exit(1)

   sent_file = open(sys.argv[1])
   tweet_file = open(sys.argv[2], 'rU')

   tweet_full = []
   for line in tweet_file:
      tweet_full.append(json.loads(line))
   tweet_file.close()

   tweet_txt = []
   print len(tweet_full)
   i = 0
   while i < len(tweet_full):
      if 'text' in tweet_full[i]:
         tweet_txt.append(tweet_full[i]['text'])
      else:
         tweet_txt.append("")
      i += 1
   print len(tweet_txt)

   afinn_dict = transform_AFINN(sent_file)
  
   tscore = assign_sentiment(tweet_txt, afinn_dict)
   print tscore
   print len(tscore)

   sys.exit(0)
   #lines(sent_file)
   #lines(tweet_file)

if __name__ == '__main__':
   main()
