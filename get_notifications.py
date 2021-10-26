from mastodon import Mastodon
import json
from html.parser import HTMLParser
from json import load as json_load


with open("/home/pi/Documents/TTIP/config.json") as file:
    config = json_load(file)
    file.close()

mastodon = Mastodon(
    access_token = config["filepath"]+'Words2Art_usercred.secret',
    api_base_url = 'https://botsin.space'
)

write_to_file=[]

class MyHTMLParser(HTMLParser):
    def handle_data(self,data):
        global write_to_file
        if str(data) != 'predetermined_images_constant' and str(data) != '@':
            write_to_file.append(data)


notis=mastodon.notifications()
parser=MyHTMLParser()
for i in notis:
    if i['type']=='mention':
        parser.feed(i['status']['content'])
    
with open(config["filepath"]+config["dictionary"],"a") as dic:
    for i in write_to_file:
        data=i.replace("\n"," ")
        if data[0] == " ":
            dic.write("\n"+data[1:len(data)])
        else:
            dic.write("\n"+data)
    dic.close()
mastodon.notifications_clear()
#[{'id': 4200626, 'type': 'follow', 'created_at': datetime.datetime(2021, 10, 25, 16, 34, 14, 283000, tzinfo=tzutc()), 'account': {'id': 106799941295060030, 'username': 'lapineGnostic', 'acct': 'lapineGnostic@plural.cafe', 'display_name': 'Bunny Girl Hazel - Burrows System', 'locked': False, 'bot': False, 'discoverable': False, 'group': False, 'created_at': datetime.datetime(2021, 8, 15, 0, 0, tzinfo=tzutc()), 'note': '<p></p>', 'url': 'https://plural.cafe/@lapineGnostic', 'avatar': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'avatar_static': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'header': 'https://botsin.space/headers/original/missing.png', 'header_static': 'https://botsin.space/headers/original/missing.png', 'followers_count': 4, 'following_count': 9, 'statuses_count': 7, 'last_status_at': datetime.datetime(2021, 10, 25, 0, 0), 'emojis': [], 'fields': []}}, {'id': 4200625, 'type': 'mention', 'created_at': datetime.datetime(2021, 10, 25, 16, 34, 5, 735000, tzinfo=tzutc()), 'account': {'id': 106799941295060030, 'username': 'lapineGnostic', 'acct': 'lapineGnostic@plural.cafe', 'display_name': 'Bunny Girl Hazel - Burrows System', 'locked': False, 'bot': False, 'discoverable': False, 'group': False, 'created_at': datetime.datetime(2021, 8, 15, 0, 0, tzinfo=tzutc()), 'note': '<p></p>', 'url': 'https://plural.cafe/@lapineGnostic', 'avatar': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'avatar_static': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'header': 'https://botsin.space/headers/original/missing.png', 'header_static': 'https://botsin.space/headers/original/missing.png', 'followers_count': 4, 'following_count': 9, 'statuses_count': 7, 'last_status_at': datetime.datetime(2021, 10, 25, 0, 0), 'emojis': [], 'fields': []}, 'status': {'id': 107163133257881580, 'created_at': datetime.datetime(2021, 10, 25, 16, 34, 5, tzinfo=tzutc()), 'in_reply_to_id': 107143079181998966, 'in_reply_to_account_id': 107129556752735263, 'sensitive': False, 'spoiler_text': '', 'visibility': 'public', 'language': 'enCafe', 'uri': 'https://plural.cafe/users/lapineGnostic/statuses/107163133226739347', 'url': 'https://plural.cafe/@lapineGnostic/107163133226739347', 'replies_count': 0, 'reblogs_count': 0, 'favourites_count': 0, 'favourited': False, 'reblogged': False, 'muted': False, 'bookmarked': False, 'content': '<p><span class="h-card"><a href="https://botsin.space/@predetermined_images_constant" class="u-url mention" rel="nofollow noopener noreferrer" target="_blank">@<span>predetermined_images_constant</span></a></span> test</p>', 'reblog': None, 'account': {'id': 106799941295060030, 'username': 'lapineGnostic', 'acct': 'lapineGnostic@plural.cafe', 'display_name': 'Bunny Girl Hazel - Burrows System', 'locked': False, 'bot': False, 'discoverable': False, 'group': False, 'created_at': datetime.datetime(2021, 8, 15, 0, 0, tzinfo=tzutc()), 'note': '<p></p>', 'url': 'https://plural.cafe/@lapineGnostic', 'avatar': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'avatar_static': 'https://files.botsin.space/cache/accounts/avatars/106/799/941/295/060/030/original/46edd4f12369bff5.jpeg', 'header': 'https://botsin.space/headers/original/missing.png', 'header_static': 'https://botsin.space/headers/original/missing.png', 'followers_count': 4, 'following_count': 9, 'statuses_count': 7, 'last_status_at': datetime.datetime(2021, 10, 25, 0, 0), 'emojis': [], 'fields': []}, 'media_attachments': [], 'mentions': [{'id': 107129556752735263, 'username': 'predetermined_images_constant', 'url': 'https://botsin.space/@predetermined_images_constant', 'acct': 'predetermined_images_constant'}], 'tags': [], 'emojis': [], 'card': None, 'poll': None}}]
