import sys
import io
import json

def extract_state(tweets):
   tweets

def transform_AFINN(sfile):
   afinn = {}
   for line in sfile:
      tmp = line.split('\t')
      afinn[tmp[0]] = tmp[1]
   return afinn

def main():
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
      if 'lang' in tweet_full[i]:
         if tweet_full[i]['lang'] == "en":
            if 'text' in tweet_full[i]:
               if 'place' in tweet_full[i]:
                  if tweet_full[i]['place'] != None:
                     if 'country' in tweet_full[i]['place']:
                        if tweet_full[i]['place']['country'] == 'United States':
                           tweet_txt.append((tweet_full[i]['text'],tweet_full[i]['place']['full_name']))
      i += 1

   print len(tweet_txt)
   for line in tweet_txt:
      print line[1].encode('utf-8')
   
   afinn_dict = transform_AFINN(sent_file)


if __name__ == '__main__':
   main()
