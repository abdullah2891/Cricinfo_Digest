import json
import praw

__author__ = 'Abdullah_Rahman'

base="http://www.espncricinfo.com"
try:

    with open("test.json") as json_file:
        json_data = json.load(json_file)



    link=json_data[0]['link']
    link_name=json_data[0]['link_name']

    s=""

    for  i in range(len(link)):
        s+= "*  ["+link_name[i]+"]"+"("+base+link[i]+")"+'\n'



    r=praw.Reddit("user_agent=digest")

    #r.login('cricinfo_bot','toolong')
    r.login('lt_snuffles','2891tanveer')
    r.submit('cricket',"Cricinfo today",s)
except ValueError:
    print "error"
    pass



