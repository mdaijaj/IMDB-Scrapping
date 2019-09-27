# scrap all actors work which language
import pprint
from imdb_task_5 import movies_name

def analysis_movies_language(movies_list):
	language_dic={}
	for i in movies_list:
		for key in i["language"]:
			if key not in language_dic:
				language_dic[key]=0
	for lan in language_dic:
		for m in movies_list:
			for l in m["language"]:
				if l==lan:
					language_dic[lan]+=1
	return(language_dic)
# pprint.pprint(analysis_movies_language(movies_name))