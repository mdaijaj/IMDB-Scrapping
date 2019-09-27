# All actors personal id scrap
from bs4 import BeautifulSoup
import pprint,requests

url="https://www.imdb.com/title/tt0066763/fullcredits?ref_=tt_cl_sm#cast"
def scrap_movie_cast(url):
	dic_list=[]
	link=requests.get(url)
	soup=BeautifulSoup(link.text,"html.parser")

	main_div=soup.find("table",class_="cast_list")
	tds=main_div.find_all("td",class_="")
	for td in tds:
		dic={}
		ids=td.find("a").get("href")[6:15]
		dic["imdb_id"]=ids
		name=td.find("a").text.strip()
		dic["name"]=name
		dic_list.append(dic)
	return(dic_list)
# pprint.pprint(scrap_movie_cast(url))