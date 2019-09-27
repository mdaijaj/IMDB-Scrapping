# scrap 250 movie details (name,rating,year,position,url from imdb website)
from bs4 import BeautifulSoup
import requests,pprint,json,os.path,random,time

def scrap_top_list():
	if os.path.exists("top_movies.json"):
		with open("top_movies.json","r") as file:
			read=file.read()
			data=json.loads(read)
		return (data)
	time.sleep(random.randint(15,30))		#for random time update
	url="https://www.imdb.com/india/top-rated-indian-movies/"
	link=requests.get(url)
	soup=BeautifulSoup(link.text,"html.parser")
	main_div=soup.find("div",class_="lister")
	tbody=main_div.find("tbody",class_="lister-list")
	trs=tbody.find_all("tr")

	movie_list=[]
	position=0
	for tr in trs:
		td=tr.find("td",class_="titleColumn")
		rating=tr.find("td",class_="ratingColumn").strong.get_text()
		name=td.find("a")
		year=td.find("span",class_="secondaryInfo")
		url=td.a["href"]
		position+=1
		movie_dic={
			"position":position,
			"name":name.text,
			"year":int(year.text[1:5]),
			"rating":rating,
			"url":"https://www.imdb.com"+url[0:17]
		}
		movie_list.append(movie_dic)

	with open("top_movies.json","w")as file:
		data=json.dump(movie_list,file,indent=4)

	return(movie_list)
# pprint.pprint(scrap_top_list())
movies = scrap_top_list()				#all movie store in movies
