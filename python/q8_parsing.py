
# coding: utf-8
#The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.


import csv

def read_data(data):
	f = open(data)
	reader = csv.reader(f)
	data = list(reader)
	f.close()
	return data

def get_min_score_difference(parsed_data):
	header = parsed_data.pop(0)
	scored = header.index('Goals')
	gave_up = header.index('Goals Allowed')
	# Start with first team as default value
	min_score_dif = int(parsed_data[0][scored])-int(parsed_data[0][gave_up])
	best_team = parsed_data[0]
    # Iterate through each team's data in parsed_data
	for team in parsed_data:
		score_dif = int(team[scored])-int(team[gave_up])
        # Computes absolute lowest dif
		if abs(score_dif) < min_score_dif:
			min_score_dif = score_dif
			best_team = team[0]
	return best_team,min_score_dif

parsed_data = read_data('football.csv')
print get_min_score_difference(parsed_data)
# ('West_Ham', -9)
