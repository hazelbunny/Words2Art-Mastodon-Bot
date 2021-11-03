import matplotlib.pyplot as plt
import numpy as np
import sys
from mastodon import Mastodon
from pathlib import Path
from json import load as json_load


with open("/home/pi/Documents/TTIP/config.json") as file:
    config = json_load(file)
    file.close()

fig, ax = plt.subplots()





class Control:
    def __init__(self):
        np.random.seed(int(config["seed"]))
        self.shapelist = 'squiggle', 'squiggle', 'line', 'squares', 'thicc_line'#,"line","dots","triangles","image"]
    def draw_random(self, key_int):
        for i in range(key_int):
            np.random.randint(1000)
        sys.stdout.flush()
        shapetype = self.shapelist[np.random.randint(key_int)%len(self.shapelist)]
        if shapetype == "squiggle":
            self.draw_squiggle(key_int,False)
        elif shapetype == "line":
            self.draw_squiggle(key_int,True)
        elif shapetype == "thicc_line":
            self.thicc_line()
        elif shapetype == "squares":
            self.draw_squares()
        #print(shapetype) #debug to see which shape is being selected after each keystroke
    def draw_squiggle(self,key_int,line):
        coords = []
        if line:
            weight = np.random.randint(1,24)/4
            sides = 2
        else:
            weight=np.random.randint(1,6)/4
            sides = np.random.randint(14,key_int+14)
        for i in range(sides):
            coords.append([np.random.randint(1000),np.random.randint(1000)])
        if sides%2==0 and line == False:
            coords.append(coords[0])
        xs, xy = zip(*coords)
        plt.plot(xs,xy,lw=weight)
    def thicc_line(self):
        plt.plot([np.random.randint(1000),np.random.randint(1000)],[np.random.randint(1000),np.random.randint(1000)],lw=np.random.randint(50,100))
    def draw_squares(self):
        for i in range(np.random.randint(1,40)):
            x=np.random.randint(1000)
            y=np.random.randint(1000)
            xoffset=(24-np.random.randint(48))/24
            yoffset=(24-np.random.randint(48))/24
            plt.plot([x+xoffset,x],[y,y+yoffset],lw=np.random.randint(20,40))
    def draw_triangles(self):
        pass
    def insert_image(self):
        pass
    def clear(self):
        sys.stdout.flush()
        np.random.seed(int(config["seed"]))
        plt.clf()
        plt.show()

with open(config["filepath"]+config["dictionary"],"r+") as dic:
    wordlist_str = dic.read()
    dic.close()

dictionary=[]
word=""
str_path=""
for i in wordlist_str:
    if i =="\n":
        dictionary.append(word)
        word=""
    else:
        word+=i
        
backup = False
if dictionary != [] and dictionary != ['']:
    chosen_word = ""
    index = -1
    while chosen_word == "" or chosen_word == " " or chosen_word == "\n":
        index +=1
        chosen_word=dictionary[index]
else:
    backup = True
    dic= open(config["filepath"]+"corncob_lowercase.txt","r+")
    wordlist_str = dic.read()
    dic.close()
    dictionary=[]
    word=""
    str_path=""
    for i in wordlist_str:
        if i =="\n":
            dictionary.append(word)
            word=""
        else:
            word+=i
    chosen_word=dictionary[np.random.randint(len(dictionary))]


canvas_control = Control()


str_path=chosen_word.replace(" ","_")
for l in chosen_word:
    canvas_control.draw_random(ord(l))
str_path=config["filepath"]+"output/"+str_path+".png"
plt.axis('off')
plt.savefig(str_path, bbox_inches='tight')
mastodon = Mastodon(
    access_token = config["filepath"]+'Words2Art_usercred.secret',
    api_base_url = 'https://botsin.space'
)
#post_file_path=Path(str_path)
#print(post_file_path)

import magic
mime = magic.from_file(str_path, mime=True)

post_file = mastodon.media_post(str_path, mime)
print(post_file)

mastodon.status_post(chosen_word,media_ids=[post_file['id']], sensitive=False)

if not backup:
    dictout=[]
    for word in wordlist_str:
        dictout.append(word)
    if not backup:
        dictionary.remove(chosen_word)
    with open(config["filepath"]+config["dictionary"],"w") as dic:
        for word in dictionary:
            dic.write(word+"\n")
        dic.close()
