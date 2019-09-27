# how many movies work actors 
from imdb_task_5 import movies_name
import pprint

def analyse_actors(movies_list):
	dic2={}
	for i in movies_list:
		for cas in i["cast"]:
			k=cas["imdb_id"]
			dic={"name":"","no_of_movies":0}
			for j in movies_list:
				n=j["cast"]
				for key in n:
					if k==key["imdb_id"]:
						dic["name"]=cas["name"]
						dic["no_of_movies"]+=1
			dic2[k]=dic
	return(dic2)				
pprint.pprint(analyse_actors(movies_name))