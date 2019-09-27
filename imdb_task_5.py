# scrap user depend input movie details (bio,time,actors and director)
from imdb_task_1 import movies
from imdb_task_13 import scrap_movie_details
import os,json,pprint


def get_movie_list_details(movies_list): 
	if os.path.exists("movies_details.json"):
		with open("movies_details.json","r") as file:
			read=file.read()
			data=json.loads(read)
		return (data)

	user=int(input("How many movies you want to scrap under 250th movies list?:"))	
	movies_ls=[]
	for j in movies_list[0:user]:
		url=j["url"]
		movies_dic=scrap_movie_details(url)
		movies_ls.append(movies_dic)
	return (movies_ls)		

	with open("movies_details.json","w")as file:
		data=json.dump(movies_ls,file,indent=4)
		write=data.write()
	return (write)
movies_name=get_movie_list_details(movies)	  #fuction call and return value
pprint.pprint(movies_name)
