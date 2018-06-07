import xml.etree.ElementTree as ET
import csv
import re

labeledTweetsFileName = 'tass_tweets/general-train-tagged.xml'
csvLabeledDataFileName = 'labeled_training_data.csv'

sentimentsMap = {
					'N': 'negativo',
					'N+': 'negativo',
					'P': 'positivo',
					'P+': 'positivo',
					'NEU': 'neutral',
					'NONE': 'neutral'
			  	}

tweetsFile = ET.parse(labeledTweetsFileName)
tweets = tweetsFile.getroot()

sentimentsCount = {
					'negativo': 0,
					'positivo': 0,
					'neutral': 0
				  }

tweetCleanupRegexp = '([@#]|http)\S*'

with open(csvLabeledDataFileName, 'a') as csvLabeledDataFile:
	csvWriter = csv.writer(csvLabeledDataFile)

	for tweet in tweets:
		tweetContent = str(tweet.findtext('content'))
		tweetContent = re.sub(tweetCleanupRegexp, '', tweetContent).strip()
		if not tweetContent:
			continue
		
		tweetSentiment = tweet.findtext('./sentiments/polarity/value')
		tweetSentiment = sentimentsMap[tweetSentiment]
		sentimentsCount[tweetSentiment] += 1
		
		csvWriter.writerow([tweetContent, tweetSentiment])

print(sentimentsCount)