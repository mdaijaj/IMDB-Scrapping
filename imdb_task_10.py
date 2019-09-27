# All director how many language work on movies
from imdb_task_5 import movies_name
import pprint

def analysis_language_and_directors(movies_list):
	director_=[]
	language_=[]
	count=0
	for i in movies_list:
		for key in i["language"]:
			if key not in language_:
				count=+1
				language_.append(key)

	for j in movies_list:
		for direc in j["director"]:
			if direc not in director_:
				director_.append(direc)

	dic1={}
	for i in director_:
		dic2={}
		for j in language_:
			count=0
			for m in movies_name:
				der=m["director"]
				lang=m["language"]
				if i in der:
					if j in lang:
						count+=1
			if count!=0:
				dic2[j]=count
		dic1[i]=dic2
	return(dic1)
# pprint.pprint(analysis_language_and_directors(movies_name))