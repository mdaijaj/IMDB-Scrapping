# Scrap all movies details base year decade

from imdb_task_1 import movies
import pprint

def group_by_decade(movie_list):
	deacade={}
	for i in movie_list:
		b=(i["year"]//10)*10
		deacade[b]=[]
	for j in deacade:
		for m in movie_list:
			year=m["year"]
			deacade[j].append(m)
	return(deacade)
# pprint.pprint(group_by_decade(movies))