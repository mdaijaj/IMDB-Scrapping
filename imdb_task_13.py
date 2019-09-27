# scrap 1 movie details (bio,time,actors and director)
from bs4 import BeautifulSoup
from imdb_task_12 import scrap_movie_cast
import pprint,requests,os,json


# scrap 1 movie details (bio,time,actors and director)
def scrap_movie_details(movie_url):
	id1=movie_url[27:-1]
	file_name=id1+".json"
	if os.path.isfile(file_name):
		with open(file_name,"r") as file1:
			read=file1.read()
			data=json.loads(read)
		return(data)
	link=requests.get(movie_url)							#call api
	soup=BeautifulSoup(link.text,"html.parser")     #convert to html form using BeautifulSoup module

	name_tag=soup.find("div",class_="title_block")	#find movie name and poster using html
	name=name_tag.find("h1").text[:-8]
	poster_tag=soup.find("div",class_="poster")
	poster=poster_tag.find("img")["src"]

	a=[]
	director=[]
	language=[]
	country=[]
	time=soup.find("div",class_="subtext")        
	run=time.find("time").text.strip()
	if run[1]=="h" and run[-3:]=="min":
		runtime=int(run[0])*60+(int(run[3:-3]))		#find runtime using slice and hour to convert into min
	else:
		runtime=run[0:-3]
		print(runtime)
	for j in time:
		if j in time.find_all("a"):					#find which type or base of movie list
			genre_list=j.text
			a.append(genre_list)
	genre=a 										#pop last element of the genre list
	genre.pop()

	summary=soup.find("div",class_="plot_summary")		
	bio=summary.find("div",class_="summary_text").text.strip()	#find bio of discription of movie

	direct_tag=summary.find("div",class_="credit_summary_item") #find all director in a movie using find_all
	direct=direct_tag.find_all("a")	
	for i in direct:
		director.append(i.text)

	article=soup.find("div", {'class' : "article", 'id':"titleDetails"})
	txt_block=article.find_all("div",class_="txt-block")
	for m in txt_block:
		b = m.find("h4", class_="inline")			#find countary and all langauage in a list
		if(b !=  None):
			if b.text=="Country:":					
				Country=m.find("a").text
			if b.text=="Language:":
				Language=m.find_all("a")
				for i in Language:
					language.append(i.text)
	abc=scrap_movie_cast(movie_url)

	all_details={									#all data is convert into dictionary
		"name":name,
		"runtime":runtime,
		"genre":genre,
		"bio":bio,
		"Country":Country,
		"poster":poster,
		"director":director,
		"language":language,
		"cast": abc
	}
	# print(all_details)

	with open(file_name,"w") as file1:
		json.dump(all_details,file1,indent=4)
	return(all_details)
url="https://www.imdb.com/title/tt0066763/"
# pprint.pprint(scrap_movie_details(url))
