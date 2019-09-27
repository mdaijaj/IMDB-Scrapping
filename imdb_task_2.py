#scrap all movies details base on year

import pprint
from imdb_task_1 import movies

def group_by_year(movie_list):			#parameter pass movie_list or anything of parameter
	years={}
	for i in movie_list:
		b=i["year"]
		years[b]=[]
	for key in years:
		for movie in movie_list:
			year=movie["year"]
			if key==year:
				years[key].append(movie)	
	return(years)
# pprint.pprint(group_by_year(movies))	#function call with arguments which store all movie list in movies
