# how many times Director work on all movies;  
from imdb_task_5 import movies_name
import pprint

def analysis_movies_directors(movie_list):
	director_dic={}
	for j in movie_list:
		for d in j["director"]:
			if d not in director_dic:
				director_dic[d] = 0
	for dirc in director_dic:
		for k in movie_list:
			for di in k['director']:
				if(di==dirc):
					director_dic[dirc]+=1
	return(director_dic)
# pprint.pprint(analysis_movies_directors(movies_name))