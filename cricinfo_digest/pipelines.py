# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import praw


class redditPipeline(object):

    def process_item(self,items,spider):
        self.team_list=items['series']
        self.teams=items['teams']
        self.score_list=items['scores']
    def open_spider(self,spider):
        pass

    def close_spider(self,spider,):
        r=praw.Reddit(user_agent='test_login')



        s=""
        s+=self.team_list[0]
        s+="* "+self.teams[0]+"   "+self.score_list[0]+'\n'



        user=raw_input("Username: ")
        password=raw_input("Password :  ")


        r.login(user,password)
        r.send_message('lt_snuffles', 'Current Scorecards',s)

