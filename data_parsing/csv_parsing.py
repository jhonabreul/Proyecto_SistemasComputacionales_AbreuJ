import csv

CSV_DATA_FILENAME = 'training_data.csv'
CSV_LABELED_DATA_FILENAME = 'training_data.csv'

POSITIVE_FEELING_ROW = 4
NEGATIVE_FEELING_ROW = 5
NEUTRAL_FEELING_ROW = 6

POSITIVE_FEELING_LABEL = 'positivo'
NEGATIVE_FEELING_LABEL = 'negativo'
NEUTRAL_FEELING_LABEL = 'neutral'

with open(CSV_DATA_FILENAME, newline = '') as csvDataFile:
	with open(CSV_LABELED_DATA_FILENAME,'w') as csvLabeledDataFile:
		csvReader = csv.reader(csvDataFile)
		csvReader.__next__() # skip header line
		for row in csvReader:
			csvLabeledDataFile.write('"' + row[POSITIVE_FEELING_ROW] + '"' + ','
									 + POSITIVE_FEELING_LABEL + '\n')
			csvLabeledDataFile.write('"' + row[NEGATIVE_FEELING_ROW] + '"' + ','
									 + NEGATIVE_FEELING_LABEL + '\n')
			csvLabeledDataFile.write('"' + row[NEUTRAL_FEELING_ROW] + '"' + ','
									 + NEUTRAL_FEELING_LABEL + '\n')
