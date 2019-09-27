# how many same actor worked on same movies :- 
from imdb_task_5 import movies_name
import pprint

def analyse_co_actors(movies_list):
	dic={}
	for i in movies_list:
		cast=i["cast"]
		dic[cast[0]["imdb_id"]]= {"Name" : cast[0]["name"], "frequent_co_actor" : []}
	for j in dic:
		for k in movies_list:
			for l in k:
				if l=="cast":
					main=k[l][0]["imdb_id"]
					if main==j:
						for ca in k[l][1:6]:
							counter=1
							for id_match in dic[j]["frequent_co_actor"]:
								if id_match["id"]==ca["imdb_id"]:
									counter+=id_match["num_movies"]							
							n={"id":ca["imdb_id"],"name":ca["name"],"num_movies":counter}
							dic[j]["frequent_co_actor"].append(n)
	return(dic)
pprint.pprint(analyse_co_actors(movies_name))