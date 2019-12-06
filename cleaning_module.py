# Libraries
import pandas as pd
import numpy as np

# Dropping duplicates 

def drop_duplicates_dataset (data):
	'''
	This function is used to drop duplicated rows that contain both the same name and artist.
	To make sure that all duplicated rows are dropped, an ouput will be printed
	The Unnamed:0 column will be dropped
	data = dataset
	'''
	data.drop_duplicates(subset=['name','artist'], inplace=True)
	data[data.duplicated(subset=['name','name'],keep=False)].count()
	x = data.drop(['Unnamed: 0'], axis=1)
	return x


# Feature Enginnering 

def extra_cleaning (data):
	'''
	length: convert length of song from milliseconds to minutes
	year: extract the year from the release_date column 
	data = dataset
	'''
	x = data['length'] = round((data ['length']/ 60000),2)
	x = data['year'] = pd.DatetimeIndex(data['release_date']).year
	x = data.drop(columns = 'Unnamed: 0',inplace=True)
	return x