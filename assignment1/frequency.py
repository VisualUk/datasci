import sys
import io
import json

def parse_file(tfile):
   tweet_full = []
   for line in tfile:
      tweet_full.append(json.loads(line))
   tweet_txt = []
   i = 0
   while i < len(tweet_full):
      if 'text' in tweet_full[i]:
         tweet_txt.append(tweet_full[i]['text'])
      else:
         tweet_txt.append("")
      i += 1
   return tweet_txt

def term_frequency(t):
   term_freq = {}
   total_wordcount = 0
   for tweet in t:
      line = tweet.split()
      for word in line:
         if word in term_freq:
            term_freq[word] = term_freq[word] + 1
            total_wordcount += 1            
         else:
            term_freq[word] = 1
            total_wordcount += 1

   term_p_freq = {}
   for word in term_freq:
      term_p_freq[word] = float(term_freq[word] / total_wordcount)

   print term_p_freq
   return term_freq
         

def main():
   tweet_file = open(sys.argv[1])
   tweets = parse_file(tweet_file)
   print tweets

   tweet_file.close()   
   term_freq = term_frequency(tweets)
   print term_freq["Facebook"]


if __name__ == '__main__':
    main()
