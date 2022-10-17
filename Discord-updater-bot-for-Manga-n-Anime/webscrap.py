from urllib import response
import requests
from bs4 import BeautifulSoup


URL = "https://w3.readone-piece.com/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")

# ! characters like "!, *, ?. @" are used for coloring comments
# ! using the "Better Comments" extension on VSCode


# ! this (site sometimes) posts LINKS before the final update
# ! must be ckecked for example check the "example.png"

# ~~~~~~~ INDICATIVE HTML CODE WITH THE LAST ATTRIBUTE (id)
# ~~~~~~~ BEFORE WHAT I NEED

# *<section id="ceo_latest_comics_widget-2" class="widget ceo_latest_comics_widget">   
#    *<h2 class="widgettitle">All Chapter</h2>
#       <ul>
#           <li>
#               <a href="https://w3.readone-piece.com/manga/one-piece-chapter-1062/">One Piece Chapter 1062 [New]🔥👹</a>
#           </li>
#           <li>
#               <a href="https://w3.readone-piece.com/manga/one-piece-chapter-1061-new%f0%9f%94%a5%f0%9f%91%b9/">One Piece Chapter 1061</a>
#           </li>
#           <li>
#               <a href="https://w3.readone-piece.com/manga/one-piece-chapter-1060-release-date/">One Piece Chapter 1060</a>
#           </li>
#           <li>
#               <a href="https://w3.readone-piece.com/manga/one-piece-chapter-1059/">One Piece Chapter 1059</a>
#           </li>
#   .../>


# hard coded ID and class for easier html parsing
id_needed       = "ceo_latest_comics_widget-2"
class_needed    =  "widgettitle"

# * respond holds the HTML text
respond = soup.find(id = id_needed)
# print("printing respond pettified")
print("======================================================================")
print("searching ceo_latest_comics_widget-2 ..... ")
print(respond.li.string)

# print(respond.prettify())


def getChapterNum(respond_str):
    # reads the string 
    # and returns the chapter number
    
    respond_str = "One Piece Chapter ".lower()
    find_str = respond.li.string.lower()
    
    if respond_str in find_str:
        # extract the chapter num
        
        chapter_num = [int(word) for word in find_str.split() if word.isdigit()]
        print(chapter_num)
        return chapter_num
    else: 
        print("something wrong in getChapterNum()")
        
           
        



# 2 states:
# 1) previous state
# 2) new state

# get the current state (== previous state) 
# * +1 (1062 => 1063) 
# then compare it with the new one 
# ! check for DOUBLE nums
# ! should consider it valid too

if getChapterNum(response) == 1063:
    # TODO:: display it to the screen
    a =''
else:
    # TODO:: display the message to the screen
    a =''
    
# TODO:find a way to keep previous states






# print the page in text format
# print(page.text)