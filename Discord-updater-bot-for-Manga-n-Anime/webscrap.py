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

# * results holds the HTML text
results = soup.find(id = id_needed)
# print("printing results pettified")
print("======================================================================")
print("searching ceo_latest_comics_widget-2 ..... ")
print("======================================================================")
print(results)
# print(results.prettify())


def get_current_state(ceo_latest):
    # ! make the string case IN-sensitive
    # parse the string till find "One Piece Chapter ", along with whitespace
    # then read
    # * 4 chars if chapter is INT
    # * or
    # * 6 if chapter is DECIMAL (dont care if it has more than 1 decimal numbers)
    print("======================================================================")
    print("get_current_state() => ceo_latest")
    print("======================================================================")
    print(ceo_latest.h3.contents[0])
    print("======================================================================")
    response = ceo_latest.h3.contents[0].lower()
    string_to_find = "One Piece Chapter ".lower()
    # ###### string_to_find.lower()
    
    
    for string in ceo_latest.strings:
        print(string)
    
    if  string_to_find in response: 
        
        print("string found")
        # * returns the LAST index of the substring found (last subcharacter of string: " ")
        last_index = lower_case_html.rindex(string_to_find) 
        print("DEBUG:: last_index: %d\n DEBUG:: last_index+1: %d", last_index, last_index+1)
        chapter_number = ""
        for i in range(last_index, last_index+4):
            chapter_number += lower_case_html[i]   
            
    else: 
        # ToDo:: catch the VAlueError 
        print("ERROR IN get_current_state:: string not found")

    

# 2 states:
# 1) previous state
# 2) new state

# get the current state (== previous state) 
# * +1 (1060 => 1061) 
# then compare it with the new one 
# ! check for DOUBLE nums
# ! should consider it valid too
get_current_state(results) 






# print the page in text format
# print(page.text)