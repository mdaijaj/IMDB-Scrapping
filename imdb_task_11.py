# scrap which type of movie
from imdb_task_5 import movies_name
import pprint

def analysis_movies_genre(movies_list):
	dic3={}
	for i in movies_list:
		for key in i["genre"]:
			dic3[key]=0
	for genre_key in dic3:
		for i in movies_list:
			for key_ in i["genre"]:
				if genre_key==key_:
					dic3[genre_key]+=1							
	return(dic3)
pprint.pprint(analysis_movies_genre(movies_name))