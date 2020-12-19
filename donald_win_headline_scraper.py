#the donald.win headline scraper

from bs4 import BeautifulSoup
import requests
import webbrowser

# basic get html function
def get_dotwin_headlines():
	url = "https://thedonald.win/"
	r = requests.get(url)
	r_html = r.text
	soup = BeautifulSoup(r_html, features="lxml")
	return soup

soup = get_dotwin_headlines()


a_list = [] # empty list to store headlines
count = 0 # counter to print number of headlines scraped

# loop through all a tags with "title" attribute to eliminate non headline links
try:
    for link in soup.findAll("a", attrs="title"):
        a_list.append(link.text.strip()) # append to empty list and strip extra lines
        print("Added...{} ".format(count) + str(link.text.strip()) + "...to the list")
        print()
        count += 1
except:
        print("The list now has " + str(count) + " headlines in it.")
        print("You can type 'headline_list' to view all headlines")
        headline_list = a_list
    
""" 1. Fix non unicode characters in title throwing errors
    2. Add try statement to tag loop so final print lines work ###DONE###
    3. Add option to basic function to change url for rising, top, and new
    """
# Code for goto website link feature

back_end_link_url = [] # empty list to store links
front_end_link_url = "https://thedonald.win"

# loop through a tags with title and href attrs to store links to titles only
for link in soup.findAll("a",attrs="title"):
	back_end_link_url.append(link.attrs["href"])

# list comp to merge title links with basic url
headline = [front_end_link_url + back_end for back_end in back_end_link_url]

# function to browse to desired headline link
def goto_thedonald(url=front_end_link_url):
	if url is not front_end_link_url:
		webbrowser.open_new_tab(url)
	else:
		webbrowser.open_new_tab(front_end_link_url)

print("*******************")
print("Use the goto_thedonald() function and pass in 'headline[x]' to jump to")
print("go to the headline of your choice. Or pass nothing to go straight to ")
print("thedonald.win. MAGA!")
print("*******************")
