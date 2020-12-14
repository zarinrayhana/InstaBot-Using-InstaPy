# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 18:32:27 2020

@author: zarin
"""
import random
from instapy import InstaPy

session = InstaPy(username='coding_student', password='Leenathz19#', headless_browser=False)
session.login()
hashtags = ['coding', 'codinglife', 'programmer', 'student', 'techstudent', 'itstudent' 'csstudent', 'codingstudent', 'studentprogrammer']
random.shuffle(hashtags)
my_tags = hashtags[:10]

session.set_do_follow(enabled = True, percentage = 90, times = 1)
session.set_do_comment(enabled=True, percentage=80)
session.set_comments([
                              'Very talented',
                              'So cool',
                              'Wow',
                              'Thats great'], media = 'Photo')
session.set_do_like(True, percentage=70)
session.set_delimit_liking(enabled=True, max_likes=200, min_likes=0)
session.set_delimit_commenting(enabled=True, max_comments=80, min_comments=0)
session.set_user_interact(amount=10, randomize=True, percentage=80)

session.like_by_tags(my_tags, amount=90, media=None)


    


    
        
                
            
            
             
                        
                
                          
            
    







